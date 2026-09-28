@pytest.mark.slow
def test_pie_series(self):
    series = Series(np.random.randint(1, 5), index=['a', 'b', 'c', 'd', 'e'], name='YLABEL')
    ax = _check_plot_works(series.plot.pie)
    self._check_text_labels(ax.texts, series.index)
    assert ax.get_ylabel() == 'YLABEL'
    ax = _check_plot_works(series.plot.pie, labels=None)
    self._check_text_labels(ax.texts, [''] * 5)
    color_args = ['r', 'g', 'b']
    ax = _check_plot_works(series.plot.pie, colors=color_args)
    color_expected = ['r', 'g', 'b', 'r', 'g']
    self._check_colors(ax.patches, facecolors=color_expected)
    labels = ['A', 'B', 'C', 'D', 'E']
    color_args = ['r', 'g', 'b', 'c', 'm']
    ax = _check_plot_works(series.plot.pie, labels=labels, colors=color_args)
    self._check_text_labels(ax.texts, labels)
    self._check_colors(ax.patches, facecolors=color_args)
    ax = _check_plot_works(series.plot.pie, colors=color_args, autopct='%.2f', fontsize=7)
    pcts = [f'{s * 100:.2f}' for s in series.values / float(series.sum())]
    expected_texts = list(chain.from_iterable(zip(series.index, pcts)))
    self._check_text_labels(ax.texts, expected_texts)
    for t in ax.texts:
        assert t.get_fontsize() == 7
    with pytest.raises(ValueError):
        series = Series([1, 2, 0, 4, -1], index=['a', 'b', 'c', 'd', 'e'])
        series.plot.pie()
    series = Series([1, 2, np.nan, 4], index=['a', 'b', 'c', 'd'], name='YLABEL')
    ax = _check_plot_works(series.plot.pie)
    self._check_text_labels(ax.texts, ['a', 'b', '', 'd'])