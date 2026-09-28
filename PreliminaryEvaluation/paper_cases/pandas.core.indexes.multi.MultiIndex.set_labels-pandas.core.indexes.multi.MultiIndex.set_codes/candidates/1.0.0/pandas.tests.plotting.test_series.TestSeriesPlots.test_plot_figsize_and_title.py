@pytest.mark.slow
def test_plot_figsize_and_title(self):
    _, ax = self.plt.subplots()
    ax = self.series.plot(title='Test', figsize=(16, 8), ax=ax)
    self._check_text_labels(ax.title, 'Test')
    self._check_axes_shape(ax, axes_num=1, layout=(1, 1), figsize=(16, 8))