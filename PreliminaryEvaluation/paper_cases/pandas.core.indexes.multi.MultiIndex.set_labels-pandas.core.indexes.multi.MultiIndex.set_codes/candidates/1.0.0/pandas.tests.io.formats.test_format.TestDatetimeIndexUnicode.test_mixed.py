def test_mixed(self):
    text = str(pd.to_datetime([datetime(2013, 1, 1), datetime(2014, 1, 1, 12), datetime(2014, 1, 1)]))
    assert "'2013-01-01 00:00:00'," in text
    assert "'2014-01-01 00:00:00']" in text