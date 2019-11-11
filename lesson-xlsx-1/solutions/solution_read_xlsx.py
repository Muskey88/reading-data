import numpy as np
import pandas as pd
import pandas.api.types as ptypes

df = pd.read_excel('playstore.xlsx', index_col=0, parse_dates=['Last Updated'])

df = df.dropna(thresh=8)
