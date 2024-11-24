from requests import get

from json import dumps
from pathlib import Path
from sys import path


# используйте свои username и personal access token (PAT)
username = 'GennDALF'
with open(r'd:\g-doc\bigbrother_cmd.pat') as filein:
    token = filein.read().strip()

params = {
    'org': "TOP-DataScience422",
    'sort': "created",
    'direction': "asc",
    'headers': {
        'X-GitHub-Api-Version': '2022-11-28'
    }
}

response = get(
    url=f'https://api.github.com/orgs/{params['org']}/repos',
    json=dumps(params),
    auth=(username, token)
)

repos = response.json()

for rep in repos:
    print(rep['name'])

# _scripts
# Andreev
# Bondarenko
# Chernenko
# Evseev
# Kursanova
# Muradli
# Piskunov
# Susljaev
# Zabivalov
# Zvereva


# проанализировать структуру данных ответа, на основании информации по каждому репозиторию составить список репозиториев, которые не обновлялись больше двух месяцев 

