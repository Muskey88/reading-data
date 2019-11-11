import numpy as np
import pandas as pd

df = pd.read_json('artist.json', orient='records')

df = df[df['paintings'] > 200]
