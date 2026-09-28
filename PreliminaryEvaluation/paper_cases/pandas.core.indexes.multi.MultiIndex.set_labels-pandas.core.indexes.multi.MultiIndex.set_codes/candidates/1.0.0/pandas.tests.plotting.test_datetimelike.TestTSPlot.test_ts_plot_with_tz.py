@pytest.mark.slow
def test_ts_plot_with_tz(self, tz_aware_fixture):
    tz = tz_aware_fixture
    index = date_range('1/1/2011', periods=2, freq='H', tz=tz)
    ts = Series([188.5, 328.25], index=index)
    _check_plot_works(ts.plot)