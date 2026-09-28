@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_format_YYYYMMDD(self, cache):
    s = Series([19801222, 19801222] + [19810105] * 5)
    expected = Series([Timestamp(x) for x in s.apply(str)])
    result = to_datetime(s, format='%Y%m%d', cache=cache)
    tm.assert_series_equal(result, expected)
    result = to_datetime(s.apply(str), format='%Y%m%d', cache=cache)
    tm.assert_series_equal(result, expected)
    expected = Series([Timestamp('19801222'), Timestamp('19801222')] + [Timestamp('19810105')] * 5)
    expected[2] = np.nan
    s[2] = np.nan
    result = to_datetime(s, format='%Y%m%d', cache=cache)
    tm.assert_series_equal(result, expected)
    s = s.apply(str)
    s[2] = 'nat'
    result = to_datetime(s, format='%Y%m%d', cache=cache)
    tm.assert_series_equal(result, expected)
    s = Series([20121231, 20141231, 99991231])
    result = pd.to_datetime(s, format='%Y%m%d', errors='ignore', cache=cache)
    expected = Series([datetime(2012, 12, 31), datetime(2014, 12, 31), datetime(9999, 12, 31)], dtype=object)
    tm.assert_series_equal(result, expected)
    result = pd.to_datetime(s, format='%Y%m%d', errors='coerce', cache=cache)
    expected = Series(['20121231', '20141231', 'NaT'], dtype='M8[ns]')
    tm.assert_series_equal(result, expected)