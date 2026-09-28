def test_constructor_pass_nan_nat(self):
    exp = Series([np.nan, np.nan], dtype=np.float64)
    assert exp.dtype == np.float64
    tm.assert_series_equal(Series([np.nan, np.nan]), exp)
    tm.assert_series_equal(Series(np.array([np.nan, np.nan])), exp)
    exp = Series([pd.NaT, pd.NaT])
    assert exp.dtype == 'datetime64[ns]'
    tm.assert_series_equal(Series([pd.NaT, pd.NaT]), exp)
    tm.assert_series_equal(Series(np.array([pd.NaT, pd.NaT])), exp)
    tm.assert_series_equal(Series([pd.NaT, np.nan]), exp)
    tm.assert_series_equal(Series(np.array([pd.NaT, np.nan])), exp)
    tm.assert_series_equal(Series([np.nan, pd.NaT]), exp)
    tm.assert_series_equal(Series(np.array([np.nan, pd.NaT])), exp)