@pytest.mark.xfail(reason='Iterator is consumed', raises=ValueError)
@pytest.mark.slow
def test_errorbar_plot_iterator(self):
    with warnings.catch_warnings():
        d = {'x': np.arange(12), 'y': np.arange(12, 0, -1)}
        df = DataFrame(d)
        ax = _check_plot_works(df.plot, yerr=itertools.repeat(0.1, len(df)))
        self._check_has_errorbars(ax, xerr=0, yerr=2)