import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('cryptos.db')

df_cryptos = pd.read_sql('''SELECT cryptocoins_cryptocurrency.name AS coin_name, cryptocoins_exchange.name AS exchange, symbol, price_usd, percent_change_7d
                            FROM cryptocoins_cryptocurrency
                            JOIN cryptocoins_exchange
                            ON cryptocoins_cryptocurrency.exchange_id = cryptocoins_exchange.id''', conn)

week_change = df.sort_values('percent_change_7d', ascending=False)
