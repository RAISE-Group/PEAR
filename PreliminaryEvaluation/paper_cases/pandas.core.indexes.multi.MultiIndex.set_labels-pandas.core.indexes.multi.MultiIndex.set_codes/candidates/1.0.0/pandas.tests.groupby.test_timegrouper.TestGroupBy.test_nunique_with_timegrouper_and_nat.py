def test_nunique_with_timegrouper_and_nat(self):
    test = pd.DataFrame({'time': [Timestamp('2016-06-28 09:35:35'), pd.NaT, Timestamp('2016-06-28 16:46:28')], 'data': ['1', '2', '3']})
    grouper = pd.Grouper(key='time', freq='h')
    result = test.groupby(grouper)['data'].nunique()
    expected = test[test.time.notnull()].groupby(grouper)['data'].nunique()
    tm.assert_series_equal(result, expected)