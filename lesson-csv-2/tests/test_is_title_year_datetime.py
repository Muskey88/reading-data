def test_is_title_year_datetime():
    assert ptypes.is_datetime64_any_dtype(df['title_year']) == True
