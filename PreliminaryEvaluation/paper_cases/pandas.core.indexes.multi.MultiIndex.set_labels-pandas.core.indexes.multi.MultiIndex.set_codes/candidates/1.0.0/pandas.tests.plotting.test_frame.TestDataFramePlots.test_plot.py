@pytest.mark.slow
def test_plot(self):
    from pandas.plotting._matplotlib.compat import _mpl_ge_3_1_0
    df = self.tdf
    _check_plot_works(df.plot, grid=False)
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.plot, subplots=True)
    self._check_axes_shape(axes, axes_num=4, layout=(4, 1))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.plot, subplots=True, layout=(-1, 2))
    self._check_axes_shape(axes, axes_num=4, layout=(2, 2))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.plot, subplots=True, use_index=False)
    self._check_axes_shape(axes, axes_num=4, layout=(4, 1))
    df = DataFrame({'x': [1, 2], 'y': [3, 4]})
    if _mpl_ge_3_1_0():
        msg = "'Line2D' object has no property 'blarg'"
    else:
        msg = 'Unknown property blarg'
    with pytest.raises(AttributeError, match=msg):
        df.plot.line(blarg=True)
    df = DataFrame(np.random.rand(10, 3), index=list(string.ascii_letters[:10]))
    _check_plot_works(df.plot, use_index=True)
    _check_plot_works(df.plot, sort_columns=False)
    _check_plot_works(df.plot, yticks=[1, 5, 10])
    _check_plot_works(df.plot, xticks=[1, 5, 10])
    _check_plot_works(df.plot, ylim=(-100, 100), xlim=(-100, 100))
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(df.plot, subplots=True, title='blah')
    axes = df.plot(subplots=True, title='blah')
    self._check_axes_shape(axes, axes_num=3, layout=(3, 1))
    for ax in axes[:2]:
        self._check_visible(ax.xaxis)
        self._check_visible(ax.get_xticklabels(), visible=False)
        self._check_visible(ax.get_xticklabels(minor=True), visible=False)
        self._check_visible([ax.xaxis.get_label()], visible=False)
    for ax in [axes[2]]:
        self._check_visible(ax.xaxis)
        self._check_visible(ax.get_xticklabels())
        self._check_visible([ax.xaxis.get_label()])
        self._check_ticks_props(ax, xrot=0)
    _check_plot_works(df.plot, title='blah')
    tuples = zip(string.ascii_letters[:10], range(10))
    df = DataFrame(np.random.rand(10, 3), index=MultiIndex.from_tuples(tuples))
    _check_plot_works(df.plot, use_index=True)
    index = MultiIndex.from_tuples([('α', 0), ('α', 1), ('β', 2), ('β', 3), ('γ', 4), ('γ', 5), ('δ', 6), ('δ', 7)], names=['i0', 'i1'])
    columns = MultiIndex.from_tuples([('bar', 'Δ'), ('bar', 'Ε')], names=['c0', 'c1'])
    df = DataFrame(np.random.randint(0, 10, (8, 2)), columns=columns, index=index)
    _check_plot_works(df.plot, title='Σ')
    df = DataFrame({'x': np.random.rand(10)})
    axes = _check_plot_works(df.plot.bar, subplots=True)
    self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
    axes = _check_plot_works(df.plot.bar, subplots=True, layout=(-1, 1))
    self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
    fig, ax = self.plt.subplots()
    axes = df.plot.bar(subplots=True, ax=ax)
    assert len(axes) == 1
    result = ax.axes
    assert result is axes[0]