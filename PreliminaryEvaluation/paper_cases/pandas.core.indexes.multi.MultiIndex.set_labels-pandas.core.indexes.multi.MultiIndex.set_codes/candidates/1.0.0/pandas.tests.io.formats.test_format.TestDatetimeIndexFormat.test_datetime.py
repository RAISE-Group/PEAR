def test_datetime(self):
    formatted = pd.to_datetime([datetime(2003, 1, 1, 12), pd.NaT]).format()
    assert formatted[0] == '2003-01-01 12:00:00'
    assert formatted[1] == 'NaT'