# Reading FIFA HTML Table

Read and store in a `DataFrame` the HTML table data in this link, https://www.fifaindex.com/players/top/fifa20_363/ it contains the top 30 FIFA players as of Oct.30, 2019.

Once the `df` is in correct format, remove the first two columns and the last one, as they are `Unnamed` and filled with NaN objects.

The `most_hits` variable should be a Series containing the player with the most amount of `Hits`.
