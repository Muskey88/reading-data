def test_last_updated_datetime():
    import pandas.api.types as ptypes
    
    assert ptypes.is_datetime64_any_dtype(df['Last_Updated']) == True
