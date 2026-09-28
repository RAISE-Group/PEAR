def test_date_explicit_date_format(self):
    formatted = pd.to_datetime([datetime(2003, 2, 1), pd.NaT]).format(date_format='%m-%d-%Y', na_rep='UT')
    assert formatted[0] == '02-01-2003'
    assert formatted[1] == 'UT'