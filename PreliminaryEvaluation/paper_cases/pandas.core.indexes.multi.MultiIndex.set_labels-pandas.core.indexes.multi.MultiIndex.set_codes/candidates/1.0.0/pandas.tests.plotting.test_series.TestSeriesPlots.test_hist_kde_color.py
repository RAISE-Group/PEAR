@pytest.mark.slow
@td.skip_if_no_scipy
def test_hist_kde_color(self):
    _, ax = self.plt.subplots()
    ax = self.ts.plot.hist(logy=True, bins=10, color='b', ax=ax)
    self._check_ax_scales(ax, yaxis='log')
    assert len(ax.patches) == 10
    self._check_colors(ax.patches, facecolors=['b'] * 10)
    _, ax = self.plt.subplots()
    ax = self.ts.plot.kde(logy=True, color='r', ax=ax)
    self._check_ax_scales(ax, yaxis='log')
    lines = ax.get_lines()
    assert len(lines) == 1
    self._check_colors(lines, ['r'])