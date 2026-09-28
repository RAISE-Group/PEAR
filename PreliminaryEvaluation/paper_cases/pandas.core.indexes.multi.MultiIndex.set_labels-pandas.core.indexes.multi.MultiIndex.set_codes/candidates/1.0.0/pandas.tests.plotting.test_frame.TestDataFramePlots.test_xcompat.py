@pytest.mark.slow
def test_xcompat(self):
    import pandas as pd
    df = self.tdf
    ax = df.plot(x_compat=True)
    lines = ax.get_lines()
    assert not isinstance(lines[0].get_xdata(), PeriodIndex)
    tm.close()
    pd.plotting.plot_params['xaxis.compat'] = True
    ax = df.plot()
    lines = ax.get_lines()
    assert not isinstance(lines[0].get_xdata(), PeriodIndex)
    tm.close()
    pd.plotting.plot_params['x_compat'] = False
    ax = df.plot()
    lines = ax.get_lines()
    assert not isinstance(lines[0].get_xdata(), PeriodIndex)
    assert isinstance(PeriodIndex(lines[0].get_xdata()), PeriodIndex)
    tm.close()
    with pd.plotting.plot_params.use('x_compat', True):
        ax = df.plot()
        lines = ax.get_lines()
        assert not isinstance(lines[0].get_xdata(), PeriodIndex)
    tm.close()
    ax = df.plot()
    lines = ax.get_lines()
    assert not isinstance(lines[0].get_xdata(), PeriodIndex)
    assert isinstance(PeriodIndex(lines[0].get_xdata()), PeriodIndex)