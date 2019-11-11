def test_gross_na.py():
    assert df.isna().sum()['gross'] == 3
