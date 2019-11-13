import numpy as np
import pandas as pd
import requests

# url variable containing the target web page
url = requests.get('https://www.fifaindex.com/players/top/fifa20_363/')

# DataFrame representing the target web page table
df = pd.read_html(url.text)

# Slice the df for correct format
df = df[0]

# Remove the first two columns and the last column
df = df.iloc[:, 2:-1]

# Create the most_hits variable containing the player with the most hits 
most_hits = df.sort_values('Hits', ascending=False).iloc[0]
