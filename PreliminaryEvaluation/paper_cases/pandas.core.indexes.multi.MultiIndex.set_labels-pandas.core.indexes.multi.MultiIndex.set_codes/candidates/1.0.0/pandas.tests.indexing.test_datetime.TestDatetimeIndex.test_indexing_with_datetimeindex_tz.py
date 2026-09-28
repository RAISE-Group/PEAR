def test_indexing_with_datetimeindex_tz(self):
    index = date_range('2015-01-01', periods=2, tz='utc')
    ser = Series(range(2), index=index, dtype='int64')
    for sel in (index, list(index)):
        tm.assert_series_equal(ser[sel], ser)
        result = ser.copy()
        result[sel] = 1
        expected = Series(1, index=index)
        tm.assert_series_equal(result, expected)
        tm.assert_series_equal(ser.loc[sel], ser)
        result = ser.copy()
        result.loc[sel] = 1
        expected = Series(1, index=index)
        tm.assert_series_equal(result, expected)
    assert ser[index[1]] == 1
    result = ser.copy()
    result[index[1]] = 5
    expected = Series([0, 5], index=index)
    tm.assert_series_equal(result, expected)
    assert ser.loc[index[1]] == 1
    result = ser.copy()
    result.loc[index[1]] = 5
    expected = Series([0, 5], index=index)
    tm.assert_series_equal(result, expected)