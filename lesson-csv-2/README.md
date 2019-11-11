# Exercise

Read and store in a `DataFrame` the data within the `movies.csv` file.

This assignment will require three steps. We will be using the same `movies.csv` as the previous exercise with different

- Check the separator used
- The column names are not in the files so we provided you with a list of the correct names.
- Missing values are encoded as `?` parse the file so those values are represented as NaN objects.
- The `budget` column has commas separating the thousands, remove those commas.
- Convert `title_year` to datetime format.
- Only movies from `USA` should be represented in the DataFrame.
