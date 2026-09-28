@pytest.mark.parametrize('m', [1, 3, 10])
@pytest.mark.parametrize('unit', ['D', 'h', 'm', 's', 'ms', 'us', 'ns'])
def test_timedelta64_conversions(self, m, unit):
    startdate = Series(pd.date_range('2013-01-01', '2013-01-03'))
    enddate = Series(pd.date_range('2013-03-01', '2013-03-03'))
    ser = enddate - startdate
    ser[2] = np.nan
    expected = Series([x / np.timedelta64(m, unit) for x in ser])
    result = ser / np.timedelta64(m, unit)
    tm.assert_series_equal(result, expected)
    expected = Series([Timedelta(np.timedelta64(m, unit)) / x for x in ser])
    result = np.timedelta64(m, unit) / ser
    tm.assert_series_equal(result, expected)