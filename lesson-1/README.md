# Exercise

Read and store in a `DataFrame` the data within the `movies.csv` file.

Take a look at the file before you load it and see what will be necessary to parse it correctly.

- Check the separator used
- The column names are not in the files so we provided you with a list of the correct names.
- Missing values are encoded as `?` parse the file so those values are represented as NaN objects.
- The `budget` column has commas separating the thousands, remove those commas.
- Skip the first 3 rows
