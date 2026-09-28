def test_to_datetime_pydatetime(self):
    actual = pd.to_datetime(datetime(2008, 1, 15))
    assert actual == datetime(2008, 1, 15)