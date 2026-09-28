@pytest.mark.slow
def test_hist_df_legacy(self):
    from matplotlib.patches import Rectangle
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(self.hist_df.hist)
    df = DataFrame(randn(100, 3))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.hist, grid=False)
    self._check_axes_shape(axes, axes_num=3, layout=(2, 2))
    assert not axes[1, 1].get_visible()
    df = DataFrame(randn(100, 1))
    _check_plot_works(df.hist)
    df = DataFrame(randn(100, 6))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.hist, layout=(4, 2))
    self._check_axes_shape(axes, axes_num=6, layout=(4, 2))
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(df.hist, sharex=True, sharey=True)
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(df.hist, figsize=(8, 10))
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(df.hist, bins=5)
    ser = df[0]
    xf, yf = (20, 18)
    xrot, yrot = (30, 40)
    axes = ser.hist(xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot)
    self._check_ticks_props(axes, xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot)
    xf, yf = (20, 18)
    xrot, yrot = (30, 40)
    axes = df.hist(xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot)
    self._check_ticks_props(axes, xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot)
    tm.close()
    ax = ser.hist(cumulative=True, bins=4, density=True)
    rects = [x for x in ax.get_children() if isinstance(x, Rectangle)]
    tm.assert_almost_equal(rects[-1].get_height(), 1.0)
    tm.close()
    ax = ser.hist(log=True)
    self._check_ax_scales(ax, yaxis='log')
    tm.close()
    with pytest.raises(AttributeError):
        ser.hist(foo='bar')