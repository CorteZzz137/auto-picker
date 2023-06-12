import requests
from bs4 import BeautifulSoup
import time
import json
from pathlib import Path

base_url = 'https://dotabuff.com'
heroes_url = base_url + '/heroes'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}
r = requests.get(heroes_url, headers=headers)

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


index = 0

for hero in heroes:
    heroRes = requests.get(base_url + hero['href'], headers=headers)
    countersRes = requests.get(
        base_url + hero['href'] + '/counters?date=week', headers=headers)
    abilitiesRes = requests.get(
        base_url + hero['href'] + '/abilities', headers=headers)

    heroSoup = BeautifulSoup(heroRes.text, 'html.parser')
    countersSoup = BeautifulSoup(countersRes.text, 'html.parser')
    abilitiesSoup = BeautifulSoup(abilitiesRes.text, 'html.parser')

    sections = abilitiesSoup.findAll('section')
    abilities = sections[:-3]
    tree = sections[-3:-2][0].find('tbody')
    main_attributes = sections[-2:-1][0].find('table', {'class': 'main'})
    other_attributes = sections[-2:-1][0].find('table', {'class': 'other'})

    parsedAbilities = []

    for i in abilities:
        parsedAbilities.append({
            'name': i.find('header').text[:-1] if i.find('header').find('big') and len(i.find('header').find('big').text) != 0 else i.find('header').text,
        })
        parsedAbilities[-1]['lowercase_name'] = '_'.join(
            parsedAbilities[-1]['name'].lower().split(' '))

        effects = i.find('div', {'class': 'effects'})
        description = i.find('div', {'class': 'description'})
        notes = i.find('div', {'class': 'notes'})
        stats = i.find('div', {'class': 'stats'})
        cooldown_and_cost = i.find('div', {'class': 'cooldown_and_cost'})
        lore = i.find('div', {'class': 'lore'})

        image_url = base_url + \
            i.find('div', {'class': 'bigavatar'}).find('img').attrs['src']
        img_data = requests.get(image_url, headers=headers).content
        folder = 'public/heroes/images/' + \
            '_'.join(hero['name'].lower().split(' '))
        Path(folder).mkdir(parents=True, exist_ok=True)
        with open(folder + '/' + parsedAbilities[-1]['lowercase_name'] + '.jpg', 'wb') as handler:
            handler.write(img_data)

        if effects:
            parsedAbilities[-1]['effects'] = [{
                'name': j.find('span').text[:-1].lower(),
                'text': j.text.split(j.find('span').text)[1]
            } for j in effects.findAll('p')]

        if description:
            parsedAbilities[-1]['description'] = description.find('p').text

        if notes:
            parsedAbilities[-1]['notes'] = [j.text for j in notes.findAll('p')]

        if stats:
            parsedAbilities[-1]['stats'] = [{
                'name': j.find('span', {'class': 'label'}).text[:-1].lower(),
                'text': j.find('span', {'class': 'values'}).text
            } for j in stats.findAll('div')]

        if cooldown_and_cost:
            cooldown = cooldown_and_cost.find('div', {'class': 'cooldown'})
            manacost = cooldown_and_cost.find('div', {'class': 'manacost'})
            if cooldown:
                parsedAbilities[-1]['cooldown'] = cooldown.find(
                    'span', {'class': 'value'}).text
            if manacost:
                parsedAbilities[-1]['manacost'] = manacost.text

        if lore:
            parsedAbilities[-1]['lore'] = lore.text

    items = []
    for header in heroSoup.findAll('header'):
        if 'Most Used Items' in header.text:
            items = header.parent.find('tbody').findAll('tr')
            break

    lane = []
    for header in heroSoup.findAll('header'):
        if 'Lane Presence' in header.text:
            lane = header.parent.find('tbody').findAll('tr')
            break

    ability_build = [-1 for i in range(18)]
    main_abilities = []
    for header in heroSoup.findAll('header'):
        if 'Most Popular Ability Build' in header.text:
            skills = [i.find('div') for i in header.parent.findAll(
                'div', {'class': 'skill'})]
            for i in range(len(skills)):
                name = skills[i].find('div', {'class': 'icon'}).find(
                    'img').attrs['alt']
                if 'Talent: ' not in name:
                    main_abilities.append(name)
                for j in skills[i].findAll('div', {'class': 'choice'}):
                    ability_build[int(j.text) - 1] = i + 1

    tree = []
    for header in heroSoup.findAll('header'):
        if 'Talent Usage' in header.text:
            rows = [row.findAll('td')[-1]
                    for row in header.parent.find('tbody').findAll('tr')]
            for row in rows:
                talents = row.findAll('div', {'class': 'talent-pw-data'})
                tree.append({
                    'left': {
                        'name': talents[0].find('span', {'class': 'talent-name-inner'}).text,
                        'pickrate': talents[0].find('div', {'class': 'talent-pick-rate'}).text.split('%')[0] + '%'
                    },
                    'right': {
                        'name': talents[1].find('span', {'class': 'talent-name-inner'}).text,
                        'pickrate': talents[1].find('div', {'class': 'talent-pick-rate'}).text.split('%')[0] + '%'
                    }
                })
            break

    data.append({
        'id': hero['id'],
        'name': hero['name'],
        'attribute': heroSoup.find('section', {'class': 'hero_attributes'}).find('tbody').get('class')[0].split('primary-')[1],
        'roles': heroSoup.find('div', {'class': 'header-content-title'}).find('small').text.split(', '),
        'winrate': heroSoup.find('div', {'class': 'header-content-secondary'}).findAll('dl')[1].find('span').text,
        'items': [{'name': i.findAll('td')[1].find('a').text, 'winrate': i.findAll('td')[-1].text} for i in items],
        'lane': [{'name': i.find('td').text, 'winrate': i.findAll('td')[2].text} for i in lane],
        'counters': [{'id': find_by_key(heroes, 'name', i.findAll('td')[1].find('a').text)[0], 'name': i.findAll('td')[1].find('a').text, 'disadvantage': i.findAll('td')[2].text} for i in countersSoup.findAll('section')[4].find('tbody').findAll('tr')],
        'lowercase_name': '_'.join(hero['name'].lower().split(' ')),
        'abilities': parsedAbilities,
        'tree': tree,
        'attributes': {
            'main': {
                'str': {
                    'base': main_attributes.find('tbody').findAll('tr')[-1].findAll('td')[0].text.split(' +')[0],
                    'increment': main_attributes.find('tbody').findAll('tr')[-1].findAll('td')[0].text.split(' +')[1]
                },
                'agi': {
                    'base': main_attributes.find('tbody').findAll('tr')[-1].findAll('td')[1].text.split(' +')[0],
                    'increment': main_attributes.find('tbody').findAll('tr')[-1].findAll('td')[1].text.split(' +')[1]
                },
                'int': {
                    'base': main_attributes.find('tbody').findAll('tr')[-1].findAll('td')[2].text.split(' +')[0],
                    'increment': main_attributes.find('tbody').findAll('tr')[-1].findAll('td')[2].text.split(' +')[1]
                }
            },
            'other': {
                'movespeed': other_attributes.findAll('tr')[0].findAll('td')[1].text,
                'armor': other_attributes.findAll('tr')[2].findAll('td')[1].text,
                'attack_time': other_attributes.findAll('tr')[3].findAll('td')[1].text,
                'damage': other_attributes.findAll('tr')[4].findAll('td')[1].text,
            }
        },
        'ability_build': ability_build,
        'main_abilities': main_abilities
    })
    index += 1
    print('обработан', data[-1]['name'], ', осталось', len(heroes) - index)
    time.sleep(0.2)

with open('public/heroes.json', 'w') as f:
    json.dump(data, f)
