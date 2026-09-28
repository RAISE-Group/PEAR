@pytest.mark.slow
def test_hist_legacy(self):
    _check_plot_works(self.ts.hist)
    _check_plot_works(self.ts.hist, grid=False)
    _check_plot_works(self.ts.hist, figsize=(8, 10))
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(self.ts.hist, by=self.ts.index.month)
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(self.ts.hist, by=self.ts.index.month, bins=5)
    fig, ax = self.plt.subplots(1, 1)
    _check_plot_works(self.ts.hist, ax=ax)
    _check_plot_works(self.ts.hist, ax=ax, figure=fig)
    _check_plot_works(self.ts.hist, figure=fig)
    tm.close()
    fig, (ax1, ax2) = self.plt.subplots(1, 2)
    _check_plot_works(self.ts.hist, figure=fig, ax=ax1)
    _check_plot_works(self.ts.hist, figure=fig, ax=ax2)
    with pytest.raises(ValueError):
        self.ts.hist(by=self.ts.index, figure=fig)