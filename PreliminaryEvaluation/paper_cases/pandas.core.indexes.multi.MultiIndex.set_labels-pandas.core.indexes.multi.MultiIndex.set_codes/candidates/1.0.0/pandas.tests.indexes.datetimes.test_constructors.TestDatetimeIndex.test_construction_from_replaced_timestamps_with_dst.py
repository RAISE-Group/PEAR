def test_construction_from_replaced_timestamps_with_dst(self):
    index = pd.date_range(pd.Timestamp(2000, 1, 1), pd.Timestamp(2005, 1, 1), freq='MS', tz='Australia/Melbourne')
    test = pd.DataFrame({'data': range(len(index))}, index=index)
    test = test.resample('Y').mean()
    result = pd.DatetimeIndex([x.replace(month=6, day=1) for x in test.index])
    expected = pd.DatetimeIndex(['2000-06-01 00:00:00', '2001-06-01 00:00:00', '2002-06-01 00:00:00', '2003-06-01 00:00:00', '2004-06-01 00:00:00', '2005-06-01 00:00:00'], tz='Australia/Melbourne')
    tm.assert_index_equal(result, expected)