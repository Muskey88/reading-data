import numpy as np
import pandas as pd

# Read in playstore.xlsx
df = pd.read_excel('playstore.xlsx', parse_dates=['Last_Updated'], usecols=['App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated'])

# Filter top 25 rated apps
df = df.sort_values('Rating', ascending=False).head(25)
