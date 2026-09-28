def test_series_plot_color_kwargs(self):
    _, ax = self.plt.subplots()
    ax = Series(np.arange(12) + 1).plot(color='green', ax=ax)
    self._check_colors(ax.get_lines(), linecolors=['green'])