import requests
from bs4 import BeautifulSoup
import time
import json

base_url = 'https://dotabuff.com'
heroesUrl = base_url + '/heroes'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}
r = requests.get(heroesUrl, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

heroes = [{'href': i.attrs['href'], 'name': i.find(
    'div', {'class': 'name'}).text} for i in soup.find('div', {'class': 'hero-grid'}).findAll('a')]

index = 0
for i in heroes:
    i['id'] = index
    index += 1

data = []


def find_by_key(iterable, key, value):
    for index, dict_ in enumerate(iterable):
        if key in dict_ and dict_[key] == value:
            return (index, dict_)


for hero in heroes:
    req = requests.get(base_url + hero['href'], headers=headers)
    req2 = requests.get(
        base_url + hero['href'] + '/counters?date=week', headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    soup2 = BeautifulSoup(req2.text, 'html.parser')
    data.append({
        'id': hero['id'],
        'name': hero['name'],
        'attribute': soup.find('section', {'class': 'hero_attributes'}).find('tbody').get('class')[0].split('primary-')[1],
        'roles': soup.find('div', {'class': 'header-content-title'}).find('small').text.split(', '),
        'winrate': soup.find('div', {'class': 'header-content-secondary'}).findAll('dl')[1].find('span').text,
        'items': [{'name': i.findAll('td')[1].find('a').text, 'winrate': i.findAll('td')[-1].text} for i in soup.findAll('section')[5].find('tbody').findAll('tr')],
        'lane': [{'name': i.find('td').text, 'winrate': i.findAll('td')[2].text} for i in soup.findAll('section')[0].find('tbody').findAll('tr')],
        'counters': [{'id': find_by_key(heroes, 'name', i.findAll('td')[1].find('a').text)[0], 'name': i.findAll('td')[1].find('a').text, 'disadvantage': i.findAll('td')[2].text} for i in soup2.findAll('section')[4].find('tbody').findAll('tr')],
        'lowercase_name': '_'.join(hero['name'].lower().split(' '))
    })
    index += 1
    print(index)
    time.sleep(0.2)

with open('static/heroes.json', 'w') as f:
    json.dump(data, f)
