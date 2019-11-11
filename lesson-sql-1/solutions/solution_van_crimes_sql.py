import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('van_crime_2003.db')

df = pd.read_sql('SELECT * FROM van_crimes', conn)

most_crimes = df[df['HUNDRED_BLOCK'] == df['HUNDRED_BLOCK'].value_counts()[:1].index[0]]
