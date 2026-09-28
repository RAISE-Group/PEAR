def test_to_datetime_YYYYMMDD(self):
    actual = pd.to_datetime('20080115')
    assert actual == datetime(2008, 1, 15)