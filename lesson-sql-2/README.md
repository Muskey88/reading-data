# Vancouver Crime advanced

- Create an sqlite3 connection to the van_crimes_2003.db SQLite3 database.
- Select TYPE, MONTH, DAY, NEIGHBOURHOOD from the `van_crimes` table, but only the observations that contain "Stanley Park" or "West End" in their `NEIGHBOURHOOD` column.
- In a `count_of_types` variable store the value counts Series of the `TYPE` column from `crimes_sp_we`.
