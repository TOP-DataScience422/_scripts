from numpy import linspace
from requests import post

from json import load, dumps
from pathlib import Path
from sys import path
from time import sleep


api_url = 'http://suggestions.dadata.ru/suggestions/api/4_1/rs/geolocate/address'
script_dir = Path(path[0])

# получить свой ключ для API dadata.ru
with open(script_dir / 'dadata_api.key') as filein:
    token = filein.read().strip()

with open(script_dir / 'dadata_reverse_geo.json') as filein:
    params = load(filein)


headers = {
    "method": "POST",
    "mode": "cors",
    "headers": {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {token}"
    },
    "body": None
}

params['lat'], params['lon'] = 56.837546, 60.598441
headers['body'] = dumps(params)
response = post(
    url=api_url,
    data=headers
)

# data = []
# for lat in linspace(56.774838, 56.914518, 100):
#     for lon in linspace(60.512302, 60.694540, 100):
#         params['lat'], params['lon'] = lat, lon
#         headers['body'] = dumps(params)
#         response = post(
#             url=api_url,
#             ? json=dumps(params),
#             ? auth=(token,)
#         )
#         data.append(response)
#         sleep(0.033)

