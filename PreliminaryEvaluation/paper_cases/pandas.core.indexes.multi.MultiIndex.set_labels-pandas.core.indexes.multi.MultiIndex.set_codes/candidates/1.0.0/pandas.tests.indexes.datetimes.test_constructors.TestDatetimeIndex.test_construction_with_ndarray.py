def test_construction_with_ndarray(self):
    dates = [datetime(2013, 10, 7), datetime(2013, 10, 8), datetime(2013, 10, 9)]
    data = DatetimeIndex(dates, freq=pd.offsets.BDay()).values
    result = DatetimeIndex(data, freq=pd.offsets.BDay())
    expected = DatetimeIndex(['2013-10-07', '2013-10-08', '2013-10-09'], freq='B')
    tm.assert_index_equal(result, expected)