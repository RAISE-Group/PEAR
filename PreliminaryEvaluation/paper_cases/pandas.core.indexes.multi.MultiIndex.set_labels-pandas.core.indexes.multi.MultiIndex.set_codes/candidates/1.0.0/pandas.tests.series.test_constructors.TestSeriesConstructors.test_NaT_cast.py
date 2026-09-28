def test_NaT_cast(self):
    result = Series([np.nan]).astype('M8[ns]')
    expected = Series([NaT])
    tm.assert_series_equal(result, expected)