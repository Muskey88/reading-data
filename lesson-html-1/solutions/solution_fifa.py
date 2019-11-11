import numpy as np
import pandas as pd
import requests

# Create the url variable containing the requests.get of the target web page
url = requests.get('https://www.fifaindex.com/players/top/fifa20_363/')

# Create a df variable
df = pd.read_html(url.text)

# Slice the df for correct format
df = df[0]

# Remove the first two columns and the last column
df = df.iloc[:, 2:-1]

# Create most_hits variable containing the player with the most hits and the number of hits he had
most_hits = df.sort_values('Hits', ascending=False).iloc[0]
