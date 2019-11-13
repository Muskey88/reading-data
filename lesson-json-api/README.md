# Swapi API to DataFrame

Swapi is Starwars REST API, we will be reading the `people` resource reading it into a Pandas DataFrame.

Use the requests library to GET the `people` resource at (https://swapi.co/api/people/?format=json)

Format the requests object into a dictionary then create a DataFrame.

When creating the `df` ensure `created` and `edited` are of datetime type.

`df_names` will contain a Pandas Series containing the `people` that are over the height of `175`.
