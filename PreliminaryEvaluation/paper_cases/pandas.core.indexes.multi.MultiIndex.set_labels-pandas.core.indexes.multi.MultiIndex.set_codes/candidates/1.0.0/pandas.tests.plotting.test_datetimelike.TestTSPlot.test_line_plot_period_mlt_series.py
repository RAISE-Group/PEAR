@pytest.mark.slow
@pytest.mark.parametrize('frqncy', ['1S', '3S', '5T', '7H', '4D', '8W', '11M', '3A'])
def test_line_plot_period_mlt_series(self, frqncy):
    idx = period_range('12/31/1999', freq=frqncy, periods=100)
    s = Series(np.random.randn(len(idx)), idx)
    _check_plot_works(s.plot, s.index.freq.rule_code)