import numpy as np
import pandas as pd

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration', 'gross', 'movie_title',
	           'num_user_for_reviews', 'country', 'cotent_rating',	'budget', 'title_year', 'imdb_score', 'genre']

# Import CSV into a DataFrame
df = pd.read_csv('movies.csv', sep='|', header=None, names=column_names, na_values='?', thousands=',', index_col='movie_title')

# Change 'year_title' data type to datetime
df['title_year'] = pd.to_datetime(df['title_year'])

# Only contain movies from 'USA' in df
df = df[df['country'] == 'USA']
