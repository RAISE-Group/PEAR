@pytest.mark.slow
def test_plot_fails_when_ax_differs_from_figure(self):
    from pylab import figure
    fig1 = figure()
    fig2 = figure()
    ax1 = fig1.add_subplot(111)
    with pytest.raises(AssertionError):
        self.ts.hist(ax=ax1, figure=fig2)