@pytest.mark.slow
@td.skip_if_no_scipy
def test_kde_kwargs(self):
    sample_points = np.linspace(-100, 100, 20)
    _check_plot_works(self.ts.plot.kde, bw_method='scott', ind=20)
    _check_plot_works(self.ts.plot.kde, bw_method=None, ind=20)
    _check_plot_works(self.ts.plot.kde, bw_method=None, ind=np.int(20))
    _check_plot_works(self.ts.plot.kde, bw_method=0.5, ind=sample_points)
    _check_plot_works(self.ts.plot.density, bw_method=0.5, ind=sample_points)
    _, ax = self.plt.subplots()
    ax = self.ts.plot.kde(logy=True, bw_method=0.5, ind=sample_points, ax=ax)
    self._check_ax_scales(ax, yaxis='log')
    self._check_text_labels(ax.yaxis.get_label(), 'Density')