@pytest.mark.slow
def test_line_plot_period_series(self):
    for s in self.period_ser:
        _check_plot_works(s.plot, s.index.freq)