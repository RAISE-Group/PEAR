def test_timedelta64_operations_with_timedeltas(self):
    td1 = Series([timedelta(minutes=5, seconds=3)] * 3)
    td2 = timedelta(minutes=5, seconds=4)
    result = td1 - td2
    expected = Series([timedelta(seconds=0)] * 3) - Series([timedelta(seconds=1)] * 3)
    assert result.dtype == 'm8[ns]'
    tm.assert_series_equal(result, expected)
    result2 = td2 - td1
    expected = Series([timedelta(seconds=1)] * 3) - Series([timedelta(seconds=0)] * 3)
    tm.assert_series_equal(result2, expected)
    tm.assert_series_equal(result + td2, td1)
    td1 = Series(pd.to_timedelta(['00:05:03'] * 3))
    td2 = pd.to_timedelta('00:05:04')
    result = td1 - td2
    expected = Series([timedelta(seconds=0)] * 3) - Series([timedelta(seconds=1)] * 3)
    assert result.dtype == 'm8[ns]'
    tm.assert_series_equal(result, expected)
    result2 = td2 - td1
    expected = Series([timedelta(seconds=1)] * 3) - Series([timedelta(seconds=0)] * 3)
    tm.assert_series_equal(result2, expected)
    tm.assert_series_equal(result + td2, td1)