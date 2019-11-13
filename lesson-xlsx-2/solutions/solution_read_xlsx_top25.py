import numpy as np
import pandas as pd

# Contain playstore.xlsx in the apps variable
apps = pd.ExcelFile('playstore.xlsx')

# 'playstore' DataFrame containing the 'Google_playstore' sheet
playstore = apps.parse(index_col=0)

# content_id DataFrame containing the `Content_ID` sheet
content_id = apps.parse('Content_ID')

# 'Google_playstore' and `Content_ID` merged into one DataFrame
df = pd.concat([playstore, content_id], axis=1)
