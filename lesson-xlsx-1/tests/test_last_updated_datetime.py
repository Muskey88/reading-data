def test_last_updated_datetime():
    assert ptypes.is_datetime64_any_dtype(df['Last Updated']) == True
