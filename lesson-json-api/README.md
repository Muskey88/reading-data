# Exercise

Read and store in a `DataFrame` the `people` resource from the Swapi Star Wars API.

- Use the requests library to GET the `people` resource at https://swapi.co/api/people/?format=json
- Format the requests object then create a DataFrame.
- When creating the `df` ensure `created` and `edited` are datetime type.
- `df_names` will contain a Series containing the people that are over the height of `175`.
