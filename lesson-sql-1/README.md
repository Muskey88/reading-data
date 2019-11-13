# Vancouver Crimes SQL to DataFrame

Read the `van_crimes` table from the SQLite database and store the information in a Pandas DataFrame.

Create an sqlite3 connection to the `van_crimes_2003.db` SQLite3 database.

Create a `df` containing the contents of the `van_crimes` table.

`street_most_instances` will contain the a <b>string</b> representing the value in `HUNDRED_BLOCK` that occurs most in `df`.

`most_crimes` will contain all observations where `HUNDRED_BLOCK` == `street_most_instances`.
