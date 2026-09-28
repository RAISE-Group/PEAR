@pytest.mark.slow
def test_line_plot_datetime_series(self):
    for s in self.datetime_ser:
        _check_plot_works(s.plot, s.index.freq.rule_code)