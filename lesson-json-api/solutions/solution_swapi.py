import numpy as np
import pandas as pd
import requests
import json
import pandas.api.types as ptypes

# Hold a requests object in the 'swapi' variable
swapi = requests.get('https://swapi.co/api/people/?format=json')

# Create a dictionary from the requests object
swapi_dict = swapi.json()

# Create a DataFrame
df = pd.DataFrame.from_dict(swapi_dict['results']).astype({'height': int})

# 'created' column is datetime type
df['created'] = pd.to_datetime(df['created'])

# Series containing the names of people with height over 175
df_names = df[df['height'] > 175]['name']
