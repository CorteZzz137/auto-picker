import requests
from bs4 import BeautifulSoup
import time
import json
from pathlib import Path

base_url = 'https://dotabuff.com'
items_url = base_url + '/items?date=week'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}
r = requests.get(items_url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
rows = soup.find('section').find('tbody').findAll('tr')

index = 0
for row in rows:
    img = row.find('img')
    src = img.attrs['src']
    name = img.attrs['title']

    image_url = base_url + src
    img_data = requests.get(image_url, headers=headers).content
    folder = 'public/items/'
    Path(folder).mkdir(parents=True, exist_ok=True)
    with open('public/items/' + '_'.join(name.lower().split(' ')) + '.jpg', 'wb') as handler:
        handler.write(img_data)
    time.sleep(0.1)
    print(index, '/', len(rows))
    index += 1
