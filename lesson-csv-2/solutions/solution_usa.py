import numpy as np
import pandas as pd
import pandas.api.types as ptypes

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration', 'gross', 'movie_title',
	           'num_user_for_reviews', 'country', 'cotent_rating',	'budget', 'title_year', 'imdb_score', 'genre']
# Import CSV
df = pd.read_csv('moives_100.csv', sep='|',  names=column_names, na_values='?', thousands=',')

# Change 'year_title' data type
df['title_year'] = pd.to_datetime(df['title_year'])

# Only contain movies from 'USA' in the DataFrame
df = df[df['country'] == 'USA']
