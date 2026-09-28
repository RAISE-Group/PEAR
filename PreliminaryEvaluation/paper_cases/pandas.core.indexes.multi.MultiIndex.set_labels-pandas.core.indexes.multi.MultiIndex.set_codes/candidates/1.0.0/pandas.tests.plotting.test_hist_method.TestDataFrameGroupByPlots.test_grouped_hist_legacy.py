@pytest.mark.slow
def test_grouped_hist_legacy(self):
    from matplotlib.patches import Rectangle
    from pandas.plotting._matplotlib.hist import _grouped_hist
    df = DataFrame(randn(500, 2), columns=['A', 'B'])
    df['C'] = np.random.randint(0, 4, 500)
    df['D'] = ['X'] * 500
    axes = _grouped_hist(df.A, by=df.C)
    self._check_axes_shape(axes, axes_num=4, layout=(2, 2))
    tm.close()
    axes = df.hist(by=df.C)
    self._check_axes_shape(axes, axes_num=4, layout=(2, 2))
    tm.close()
    axes = df.hist(by='D', rot=30)
    self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
    self._check_ticks_props(axes, xrot=30)
    tm.close()
    xf, yf = (20, 18)
    xrot, yrot = (30, 40)
    axes = _grouped_hist(df.A, by=df.C, cumulative=True, bins=4, xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot, density=True)
    for ax in axes.ravel():
        rects = [x for x in ax.get_children() if isinstance(x, Rectangle)]
        height = rects[-1].get_height()
        tm.assert_almost_equal(height, 1.0)
    self._check_ticks_props(axes, xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot)
    tm.close()
    axes = _grouped_hist(df.A, by=df.C, log=True)
    self._check_ax_scales(axes, yaxis='log')
    tm.close()
    with pytest.raises(AttributeError):
        _grouped_hist(df.A, by=df.C, foo='bar')
    msg = 'Specify figure size by tuple instead'
    with pytest.raises(ValueError, match=msg):
        df.hist(by='C', figsize='default')