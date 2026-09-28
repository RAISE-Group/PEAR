@pytest.mark.slow
def test_autocorrelation_plot(self):
    from pandas.plotting import autocorrelation_plot
    _check_plot_works(autocorrelation_plot, series=self.ts)
    _check_plot_works(autocorrelation_plot, series=self.ts.values)
    ax = autocorrelation_plot(self.ts, label='Test')
    self._check_legend_labels(ax, labels=['Test'])