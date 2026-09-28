@pytest.mark.slow
def test_boxplot(self):
    df = self.hist_df
    series = df['height']
    numeric_cols = df._get_numeric_data().columns
    labels = [pprint_thing(c) for c in numeric_cols]
    ax = _check_plot_works(df.plot.box)
    self._check_text_labels(ax.get_xticklabels(), labels)
    tm.assert_numpy_array_equal(ax.xaxis.get_ticklocs(), np.arange(1, len(numeric_cols) + 1))
    assert len(ax.lines) == self.bp_n_objects * len(numeric_cols)
    axes = series.plot.box(rot=40)
    self._check_ticks_props(axes, xrot=40, yrot=0)
    tm.close()
    ax = _check_plot_works(series.plot.box)
    positions = np.array([1, 6, 7])
    ax = df.plot.box(positions=positions)
    numeric_cols = df._get_numeric_data().columns
    labels = [pprint_thing(c) for c in numeric_cols]
    self._check_text_labels(ax.get_xticklabels(), labels)
    tm.assert_numpy_array_equal(ax.xaxis.get_ticklocs(), positions)
    assert len(ax.lines) == self.bp_n_objects * len(numeric_cols)