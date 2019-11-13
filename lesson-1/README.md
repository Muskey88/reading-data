# Reading movies CSV

Read and store in a `DataFrame` the data within the `movies.csv` file.

Take a look at the file before you read it into a DataFrame and see what will be necessary to parse it correctly.

- Check the separator used
- The column names are not in the files so we provided you with a list of the correct names.
- Missing values are encoded as `?` parse the file so those values are represented as NaN objects.
- The `budget` column has commas separating the thousands, make sure the column is of float data type.
- Skip the first 3 rows.

This CSV is altered for this course and originally from Kaggle, https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset
