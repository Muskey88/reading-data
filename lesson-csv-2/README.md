# Reading Movies CSV with DataFrame manipulation

Read and store in a `DataFrame` the data within the `movies.csv` file.

This assignment will require a few extra steps. We will be using the same `movies.csv` as the previous exercise.

- Check the separator used
- The column names are not in the files so we provided you with a list of the correct names.
- Missing values are encoded as `?` parse the file so those values are represented as NaN objects.
- The `budget` column has commas separating the thousands, remove those commas.
- Convert `title_year` to datetime format.
- Only movies from `USA` should be represented in the DataFrame.
- The index of the DataFrame should be represented by the `movie_title` column.

This CSV is altered for this course and originally from Kaggle, https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset
