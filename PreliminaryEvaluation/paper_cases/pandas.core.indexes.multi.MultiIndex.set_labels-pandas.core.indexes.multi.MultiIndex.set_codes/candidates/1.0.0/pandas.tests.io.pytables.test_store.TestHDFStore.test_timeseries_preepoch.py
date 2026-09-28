def test_timeseries_preepoch(self, setup_path):
    dr = bdate_range('1/1/1940', '1/1/1960')
    ts = Series(np.random.randn(len(dr)), index=dr)
    try:
        self._check_roundtrip(ts, tm.assert_series_equal, path=setup_path)
    except OverflowError:
        pytest.skip('known failer on some windows platforms')