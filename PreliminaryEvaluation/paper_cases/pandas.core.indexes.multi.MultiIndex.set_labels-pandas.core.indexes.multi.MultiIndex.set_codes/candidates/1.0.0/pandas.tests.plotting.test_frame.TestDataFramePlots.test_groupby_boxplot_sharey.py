def test_groupby_boxplot_sharey(self):
    df = DataFrame({'a': [-1.43, -0.15, -3.7, -1.43, -0.14], 'b': [0.56, 0.84, 0.29, 0.56, 0.85], 'c': [0, 1, 2, 3, 1]}, index=[0, 1, 2, 3, 4])
    axes = df.groupby('c').boxplot()
    expected = [True, False, True, False]
    self._assert_ytickslabels_visibility(axes, expected)
    axes = df.groupby('c').boxplot(sharey=True)
    expected = [True, False, True, False]
    self._assert_ytickslabels_visibility(axes, expected)
    axes = df.groupby('c').boxplot(sharey=False)
    expected = [True, True, True, True]
    self._assert_ytickslabels_visibility(axes, expected)