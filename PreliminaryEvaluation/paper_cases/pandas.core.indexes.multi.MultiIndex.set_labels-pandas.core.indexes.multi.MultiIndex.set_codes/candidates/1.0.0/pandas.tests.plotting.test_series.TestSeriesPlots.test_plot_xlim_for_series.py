@pytest.mark.parametrize('kind', ['line', 'area'])
def test_plot_xlim_for_series(self, kind):
    s = Series([2, 3])
    _, ax = self.plt.subplots()
    s.plot(kind=kind, ax=ax)
    xlims = ax.get_xlim()
    assert xlims[0] < 0
    assert xlims[1] > 1