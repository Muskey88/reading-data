def test_country_unique():
    assert np.array_equal(df['country'].unique(), np.array(['USA'], dtype=object))
