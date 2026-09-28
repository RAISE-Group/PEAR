def test_all_nans(self):
    result = Series([np.nan]).asof([0])
    expected = Series([np.nan])
    tm.assert_series_equal(result, expected)
    N = 50
    rng = date_range('1/1/1990', periods=N, freq='53s')
    dates = date_range('1/1/1990', periods=N * 3, freq='25s')
    result = Series(np.nan, index=rng).asof(dates)
    expected = Series(np.nan, index=dates)
    tm.assert_series_equal(result, expected)
    date = date_range('1/1/1990', periods=N * 3, freq='25s')[0]
    result = Series(np.nan, index=rng).asof(date)
    assert isna(result)
    result = Series(np.nan, index=[1, 2, 3, 4], name='test').asof([4, 5])
    expected = Series(np.nan, index=[4, 5], name='test')
    tm.assert_series_equal(result, expected)