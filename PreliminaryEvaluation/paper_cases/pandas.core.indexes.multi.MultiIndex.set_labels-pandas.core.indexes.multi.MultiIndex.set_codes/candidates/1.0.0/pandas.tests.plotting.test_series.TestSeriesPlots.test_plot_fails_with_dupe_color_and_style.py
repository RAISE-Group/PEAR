@pytest.mark.slow
def test_plot_fails_with_dupe_color_and_style(self):
    x = Series(randn(2))
    with pytest.raises(ValueError):
        _, ax = self.plt.subplots()
        x.plot(style='k--', color='k', ax=ax)