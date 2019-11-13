def test_df_name():
    assert np.array_equal(df['name'].values,
    np.array(['Amedeo Modigliani', 'Rene Magritte'], dtype=object))
