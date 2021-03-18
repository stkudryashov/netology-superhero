import requests
import time

from api_token import token


heroes = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}

for hero in heroes.keys():
    response = requests.get(f'https://superheroapi.com/api/{token}/search/{hero}')
    heroes[hero] = int(response.json()['results'][0]['powerstats']['intelligence'])
    time.sleep(0.3)

print(heroes)
max_intel = max(heroes, key=heroes.get)
print('Max intelligence:', max_intel, heroes.get(max_intel))
