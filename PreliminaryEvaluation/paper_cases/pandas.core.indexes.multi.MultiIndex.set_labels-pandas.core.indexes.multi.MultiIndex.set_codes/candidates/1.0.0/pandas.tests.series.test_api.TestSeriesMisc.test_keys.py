def test_keys(self, datetime_series):
    getkeys = datetime_series.keys
    assert getkeys() is datetime_series.index