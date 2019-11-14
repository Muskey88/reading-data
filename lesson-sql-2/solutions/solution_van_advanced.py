import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('van_crime_2003.db')

crimes_sp_we = pd.read_sql('''SELECT TYPE, MONTH, DAY, NEIGHBOURHOOD
                              FROM van_crimes WHERE NEIGHBOURHOOD IN ("Stanley Park", "West End")''', conn)

count_of_types = crimes_sp_we['TYPE'].value_counts()
