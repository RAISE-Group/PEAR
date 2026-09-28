@pytest.mark.slow
def test_boxplot_series(self):
    _, ax = self.plt.subplots()
    ax = self.ts.plot.box(logy=True, ax=ax)
    self._check_ax_scales(ax, yaxis='log')
    xlabels = ax.get_xticklabels()
    self._check_text_labels(xlabels, [self.ts.name])
    ylabels = ax.get_yticklabels()
    self._check_text_labels(ylabels, [''] * len(ylabels))