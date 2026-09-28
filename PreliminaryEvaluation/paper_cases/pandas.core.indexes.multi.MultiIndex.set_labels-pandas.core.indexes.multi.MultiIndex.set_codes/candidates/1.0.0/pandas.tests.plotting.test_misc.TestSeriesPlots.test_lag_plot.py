@pytest.mark.slow
def test_lag_plot(self):
    from pandas.plotting import lag_plot
    _check_plot_works(lag_plot, series=self.ts)
    _check_plot_works(lag_plot, series=self.ts, lag=5)