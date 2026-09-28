@pytest.mark.slow
def test_hist_df(self):
    from matplotlib.patches import Rectangle
    df = DataFrame(randn(100, 4))
    series = df[0]
    ax = _check_plot_works(df.plot.hist)
    expected = [pprint_thing(c) for c in df.columns]
    self._check_legend_labels(ax, labels=expected)
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.plot.hist, subplots=True, logy=True)
    self._check_axes_shape(axes, axes_num=4, layout=(4, 1))
    self._check_ax_scales(axes, yaxis='log')
    axes = series.plot.hist(rot=40)
    self._check_ticks_props(axes, xrot=40, yrot=0)
    tm.close()
    ax = series.plot.hist(cumulative=True, bins=4, density=True)
    rects = [x for x in ax.get_children() if isinstance(x, Rectangle)]
    tm.assert_almost_equal(rects[-1].get_height(), 1.0)
    tm.close()
    ax = series.plot.hist(cumulative=True, bins=4)
    rects = [x for x in ax.get_children() if isinstance(x, Rectangle)]
    tm.assert_almost_equal(rects[-2].get_height(), 100.0)
    tm.close()
    axes = df.plot.hist(rot=50, fontsize=8, orientation='horizontal')
    self._check_ticks_props(axes, xrot=0, yrot=50, ylabelsize=8)