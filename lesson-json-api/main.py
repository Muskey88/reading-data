import numpy as np
import pandas as pd
import requests
import json
import pandas.api.types as ptypes

# Hold a requests object in the 'swapi' variable
swapi = requests.get('')

# Create a dictionary from the requests object
swapi_dict = ...

# Create a DataFrame
df = ....astype({'height': int})

# 'created' column is datetime type
df['created'] = ...

# Series containing the names of people with height over 175
df_names = ...
