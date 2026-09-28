def test_isnull_for_inf_deprecated(self):
    s = Series(['a', np.inf, np.nan, 1.0])
    with pd.option_context('mode.use_inf_as_null', True):
        r = s.isna()
        dr = s.dropna()
    e = Series([False, True, True, False])
    de = Series(['a', 1.0], index=[0, 3])
    tm.assert_series_equal(r, e)
    tm.assert_series_equal(dr, de)