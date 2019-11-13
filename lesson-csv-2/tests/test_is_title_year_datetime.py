def test_is_title_year_datetime():
    import pandas.api.types as ptypes
    
    assert ptypes.is_datetime64_any_dtype(df['title_year']) == True
