def test_created_edited_dtime():
    assert ptypes.is_datetime64_any_dtype(df['created']) == True
    assert ptypes.is_datetime64_any_dtype(df['edited']) == True
