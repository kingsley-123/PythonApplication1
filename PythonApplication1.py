import requests
import json
import pandas as pd

def call_api(url):
    response = requests.get(url)
    data = response.json()
    return data

def details(data):
    checklist = []
    for x in data['results']:
        char = {'name' : x['name'], 'no_episode' : x['episode']}
        checklist.append(char)
    return checklist

mainlist = []
data = call_api(f'https://rickandmortyapi.com/api/character')
for x in range(1,data['info']['pages']+1):
    page_num = x * 1
    data = call_api(f'https://rickandmortyapi.com/api/character?page={page_num}')
    mainlist.extend(details(data))
    
df = pd.DataFrame(mainlist)
print(df)
