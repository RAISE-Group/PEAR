@pytest.mark.slow
def test_boxplot_vertical(self):
    df = self.hist_df
    numeric_cols = df._get_numeric_data().columns
    labels = [pprint_thing(c) for c in numeric_cols]
    ax = df.plot.box(rot=50, fontsize=8, vert=False)
    self._check_ticks_props(ax, xrot=0, yrot=50, ylabelsize=8)
    self._check_text_labels(ax.get_yticklabels(), labels)
    assert len(ax.lines) == self.bp_n_objects * len(numeric_cols)
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.plot.box, subplots=True, vert=False, logx=True)
    self._check_axes_shape(axes, axes_num=3, layout=(1, 3))
    self._check_ax_scales(axes, xaxis='log')
    for ax, label in zip(axes, labels):
        self._check_text_labels(ax.get_yticklabels(), [label])
        assert len(ax.lines) == self.bp_n_objects
    positions = np.array([3, 2, 8])
    ax = df.plot.box(positions=positions, vert=False)
    self._check_text_labels(ax.get_yticklabels(), labels)
    tm.assert_numpy_array_equal(ax.yaxis.get_ticklocs(), positions)
    assert len(ax.lines) == self.bp_n_objects * len(numeric_cols)