def test_to_datetime_unparseable_ignore(self):
    s = 'Month 1, 1999'
    assert pd.to_datetime(s, errors='ignore') == s