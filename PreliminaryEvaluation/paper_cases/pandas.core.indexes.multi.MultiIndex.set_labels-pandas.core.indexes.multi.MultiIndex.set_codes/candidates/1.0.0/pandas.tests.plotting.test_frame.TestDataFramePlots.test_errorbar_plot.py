@pytest.mark.slow
def test_errorbar_plot(self):
    with warnings.catch_warnings():
        d = {'x': np.arange(12), 'y': np.arange(12, 0, -1)}
        df = DataFrame(d)
        d_err = {'x': np.ones(12) * 0.2, 'y': np.ones(12) * 0.4}
        df_err = DataFrame(d_err)
        ax = _check_plot_works(df.plot, yerr=df_err, logy=True)
        self._check_has_errorbars(ax, xerr=0, yerr=2)
        ax = _check_plot_works(df.plot, yerr=df_err, logx=True, logy=True)
        self._check_has_errorbars(ax, xerr=0, yerr=2)
        ax = _check_plot_works(df.plot, yerr=df_err, loglog=True)
        self._check_has_errorbars(ax, xerr=0, yerr=2)
        kinds = ['line', 'bar', 'barh']
        for kind in kinds:
            ax = _check_plot_works(df.plot, yerr=df_err['x'], kind=kind)
            self._check_has_errorbars(ax, xerr=0, yerr=2)
            ax = _check_plot_works(df.plot, yerr=d_err, kind=kind)
            self._check_has_errorbars(ax, xerr=0, yerr=2)
            ax = _check_plot_works(df.plot, yerr=df_err, xerr=df_err, kind=kind)
            self._check_has_errorbars(ax, xerr=2, yerr=2)
            ax = _check_plot_works(df.plot, yerr=df_err['x'], xerr=df_err['x'], kind=kind)
            self._check_has_errorbars(ax, xerr=2, yerr=2)
            ax = _check_plot_works(df.plot, xerr=0.2, yerr=0.2, kind=kind)
            self._check_has_errorbars(ax, xerr=2, yerr=2)
            axes = _check_plot_works(df.plot, yerr=df_err, xerr=df_err, subplots=True, kind=kind)
            self._check_has_errorbars(axes, xerr=1, yerr=1)
        ax = _check_plot_works((df + 1).plot, yerr=df_err, xerr=df_err, kind='bar', log=True)
        self._check_has_errorbars(ax, xerr=2, yerr=2)
        ax = _check_plot_works(df['y'].plot, yerr=np.ones(12) * 0.4)
        self._check_has_errorbars(ax, xerr=0, yerr=1)
        ax = _check_plot_works(df.plot, yerr=np.ones((2, 12)) * 0.4)
        self._check_has_errorbars(ax, xerr=0, yerr=2)
        for yerr in ['yerr', '誤差']:
            s_df = df.copy()
            s_df[yerr] = np.ones(12) * 0.2
            ax = _check_plot_works(s_df.plot, yerr=yerr)
            self._check_has_errorbars(ax, xerr=0, yerr=2)
            ax = _check_plot_works(s_df.plot, y='y', x='x', yerr=yerr)
            self._check_has_errorbars(ax, xerr=0, yerr=1)
        with pytest.raises(ValueError):
            df.plot(yerr=np.random.randn(11))
        df_err = DataFrame({'x': ['zzz'] * 12, 'y': ['zzz'] * 12})
        with pytest.raises((ValueError, TypeError)):
            df.plot(yerr=df_err)