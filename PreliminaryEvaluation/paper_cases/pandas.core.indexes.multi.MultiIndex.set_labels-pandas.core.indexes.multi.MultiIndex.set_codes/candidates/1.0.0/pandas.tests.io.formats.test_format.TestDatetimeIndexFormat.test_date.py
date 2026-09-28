def test_date(self):
    formatted = pd.to_datetime([datetime(2003, 1, 1), pd.NaT]).format()
    assert formatted[0] == '2003-01-01'
    assert formatted[1] == 'NaT'