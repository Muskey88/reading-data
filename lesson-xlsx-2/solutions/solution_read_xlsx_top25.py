import numpy as np
import pandas as pd
import pandas.api.types as ptypes

df = pd.read_excel('playstore.xlsx', parse_dates=['Last Updated'], usecols=['App', 'Rating', 'Installs', 'Content Rating', 'Genres', 'Last Updated'])

df = df.sort_values('Rating', ascending=False).head(25)
