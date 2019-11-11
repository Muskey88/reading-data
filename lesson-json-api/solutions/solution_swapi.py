import numpy as np
import pandas as pd
import requests
import json
import pandas.api.types as ptypes

url = requests.get('https://swapi.co/api/people/?format=json')

url_json = json.dumps(url.json()['results'])

df = pd.read_json(url_json, convert_dates=['created', 'edited'])

df_names = df[df['height'] > 175]['name']
