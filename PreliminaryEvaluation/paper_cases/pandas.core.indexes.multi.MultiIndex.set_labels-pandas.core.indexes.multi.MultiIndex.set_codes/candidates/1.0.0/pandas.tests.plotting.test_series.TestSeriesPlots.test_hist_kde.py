@pytest.mark.slow
@td.skip_if_no_scipy
def test_hist_kde(self):
    _, ax = self.plt.subplots()
    ax = self.ts.plot.hist(logy=True, ax=ax)
    self._check_ax_scales(ax, yaxis='log')
    xlabels = ax.get_xticklabels()
    self._check_text_labels(xlabels, [''] * len(xlabels))
    ylabels = ax.get_yticklabels()
    self._check_text_labels(ylabels, [''] * len(ylabels))
    _check_plot_works(self.ts.plot.kde)
    _check_plot_works(self.ts.plot.density)
    _, ax = self.plt.subplots()
    ax = self.ts.plot.kde(logy=True, ax=ax)
    self._check_ax_scales(ax, yaxis='log')
    xlabels = ax.get_xticklabels()
    self._check_text_labels(xlabels, [''] * len(xlabels))
    ylabels = ax.get_yticklabels()
    self._check_text_labels(ylabels, [''] * len(ylabels))