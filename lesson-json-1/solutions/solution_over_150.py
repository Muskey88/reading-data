import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize

# Parse the JSON file into a Python dictionary
with open('artists.json') as file:
    artists_dict = json.load(file)

# Unpack the `bio` column into a DataFrame, include the `name` column
bio_df = json_normalize(artists_dict, record_path='bio', meta='name')

# df should contain artists that have greater than 150 paintings
df = bio_df[bio_df['paintings'] > 150]
