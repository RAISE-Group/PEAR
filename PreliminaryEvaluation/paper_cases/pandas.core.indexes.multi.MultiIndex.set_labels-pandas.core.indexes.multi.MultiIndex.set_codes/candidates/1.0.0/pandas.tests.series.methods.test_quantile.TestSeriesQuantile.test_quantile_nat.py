def test_quantile_nat(self):
    res = Series([pd.NaT, pd.NaT]).quantile(0.5)
    assert res is pd.NaT
    res = Series([pd.NaT, pd.NaT]).quantile([0.5])
    tm.assert_series_equal(res, pd.Series([pd.NaT], index=[0.5]))