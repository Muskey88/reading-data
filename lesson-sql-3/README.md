# Crypto currency relational database

We have SQLite3 database containing two tables as seen in the table below. `cryptocoins_cryptocurrency` and `cryptocoins_exchange` the `exchange_id` field a foreign key, representing the `id` primary key of `cryptocoins_exchange`.

Create an sqlite3 connection to the `cryptos.db` SQLite3 database.

This is going to be a complex query so the description will be in detail.
- Because both tables have a `name` column we must assign alternate names in the query.
- Select the `name` from `cryptocoins_cryptocurrency.name` as `coin_name`.
- `cryptocoins_exchange.name` as `exchange`.
- and `symbol, price_usd, percent_change_7d`.
- From `cryptocoins_cryptocurrency`.
- Joining with `cryptocoins_exchange`.
- On the `exchange_id` and the `id` of `cryptocoins_exchange`.

Once you have the DataFrame, sort it by `percent_change_7d` from highest to lowest and assign that to `week_change`.


<p align="center">
  <img width="600px" src="https://lh3.googleusercontent.com/f0NKiFW0vwT01eAurSVMLs10HXLiout-6u3BnADmc_U1NU5rcKCMd3zHCfmNYHnjDyoA20um07mnQblX0IH3EEfG2flCB-8slct4DqOjle4Jc-PeG4uaKyLfcfPS0eSvnIQh9Oc6c3IdrkOWScxv5P0KVmJkZYolldiskYk4ZXJciKh8Dnm5YMtYPHk-1nZ2YOSddshhLwL63K-dfe5DR43g6dtN-m2iqDgyPRZgIJemk8bA-hscdNIdUK94kGKEZhVschpPJp6Ae3eYZSti7qWLjLjp371tqnuu727cTv-L1AGLByfpE1axoj3KeLOaBaxHigpFFhmG2e_gb1DVagMndHf5otdRNgktWC1y1d64k9we5XRBRYyXW9b-6whcOWz8WHw0s8gJWKIaPIw8CgZkZzaCSU9EtfUccTEkGD0KIPqJeT701vQpGOV080nZlVlG27d6DIGTeSoj6EvKl6Qmfpel01NucUvkQJylkwqm90eMcM6ysS0zuZs_x-4kQXjbijJoP6SS4t01ELaGhjheUcFG9oc2PYW7YijZKxQQN7aEg1zmHM_jSmILwz_GDhjtjt50hI61GtinGg82Y1M8E9WdBPQ1R9IFig6YR3ijm0cYCUgdZIl8GAYDZQqfIsOfxBAAhSWINiH80M2DYe-thrb_qdMoVDXpQzKGzAZU5NQOvY2GcaM=w585-h604-no">
</p>
