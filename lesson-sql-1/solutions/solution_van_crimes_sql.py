import numpy as np
import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('van_crime_2003.db')

# Create DataFrame
df = pd.read_sql('SELECT * FROM van_crimes', conn)

# Most instances in 'HUNDRED_BLOCK'
street_most_instances = df['HUNDRED_BLOCK'].value_counts()[:1].index[0]

# Observations from street_most_instances
most_crimes = df[df['HUNDRED_BLOCK'] == street_most_instances]
