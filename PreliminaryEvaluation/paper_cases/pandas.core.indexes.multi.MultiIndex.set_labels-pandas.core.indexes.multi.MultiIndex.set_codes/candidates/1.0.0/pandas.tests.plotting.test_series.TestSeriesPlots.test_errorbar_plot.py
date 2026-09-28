@pytest.mark.slow
def test_errorbar_plot(self):
    s = Series(np.arange(10), name='x')
    s_err = np.random.randn(10)
    d_err = DataFrame(randn(10, 2), index=s.index, columns=['x', 'y'])
    kinds = ['line', 'bar']
    for kind in kinds:
        ax = _check_plot_works(s.plot, yerr=Series(s_err), kind=kind)
        self._check_has_errorbars(ax, xerr=0, yerr=1)
        ax = _check_plot_works(s.plot, yerr=s_err, kind=kind)
        self._check_has_errorbars(ax, xerr=0, yerr=1)
        ax = _check_plot_works(s.plot, yerr=s_err.tolist(), kind=kind)
        self._check_has_errorbars(ax, xerr=0, yerr=1)
        ax = _check_plot_works(s.plot, yerr=d_err, kind=kind)
        self._check_has_errorbars(ax, xerr=0, yerr=1)
        ax = _check_plot_works(s.plot, xerr=0.2, yerr=0.2, kind=kind)
        self._check_has_errorbars(ax, xerr=1, yerr=1)
    ax = _check_plot_works(s.plot, xerr=s_err)
    self._check_has_errorbars(ax, xerr=1, yerr=0)
    ix = date_range('1/1/2000', '1/1/2001', freq='M')
    ts = Series(np.arange(12), index=ix, name='x')
    ts_err = Series(np.random.randn(12), index=ix)
    td_err = DataFrame(randn(12, 2), index=ix, columns=['x', 'y'])
    ax = _check_plot_works(ts.plot, yerr=ts_err)
    self._check_has_errorbars(ax, xerr=0, yerr=1)
    ax = _check_plot_works(ts.plot, yerr=td_err)
    self._check_has_errorbars(ax, xerr=0, yerr=1)
    with pytest.raises(ValueError):
        s.plot(yerr=np.arange(11))
    s_err = ['zzz'] * 10
    with pytest.raises(TypeError):
        s.plot(yerr=s_err)