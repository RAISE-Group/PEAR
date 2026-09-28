@pytest.mark.parametrize('kind', ['line', 'area'])
def test_xlim_plot_line(self, kind):
    df = pd.DataFrame([2, 4], index=[1, 2])
    ax = df.plot(kind=kind)
    xlims = ax.get_xlim()
    assert xlims[0] < 1
    assert xlims[1] > 2