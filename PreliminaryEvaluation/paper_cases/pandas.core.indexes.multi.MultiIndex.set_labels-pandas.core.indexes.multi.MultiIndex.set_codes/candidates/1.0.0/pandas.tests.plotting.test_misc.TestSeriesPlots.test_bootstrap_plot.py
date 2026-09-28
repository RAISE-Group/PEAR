@pytest.mark.slow
def test_bootstrap_plot(self):
    from pandas.plotting import bootstrap_plot
    _check_plot_works(bootstrap_plot, series=self.ts, size=10)