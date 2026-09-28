def test_datetimeindex(self):
    idx1 = pd.DatetimeIndex(['2013-04-01 9:00', '2013-04-02 9:00', '2013-04-03 9:00'] * 2, tz='Asia/Tokyo')
    idx2 = pd.date_range('2010/01/01', periods=6, freq='M', tz='US/Eastern')
    idx = MultiIndex.from_arrays([idx1, idx2])
    expected1 = pd.DatetimeIndex(['2013-04-01 9:00', '2013-04-02 9:00', '2013-04-03 9:00'], tz='Asia/Tokyo')
    tm.assert_index_equal(idx.levels[0], expected1)
    tm.assert_index_equal(idx.levels[1], idx2)
    date1 = datetime.date.today()
    date2 = datetime.datetime.today()
    date3 = Timestamp.today()
    for d1, d2 in itertools.product([date1, date2, date3], [date1, date2, date3]):
        index = MultiIndex.from_product([[d1], [d2]])
        assert isinstance(index.levels[0], pd.DatetimeIndex)
        assert isinstance(index.levels[1], pd.DatetimeIndex)