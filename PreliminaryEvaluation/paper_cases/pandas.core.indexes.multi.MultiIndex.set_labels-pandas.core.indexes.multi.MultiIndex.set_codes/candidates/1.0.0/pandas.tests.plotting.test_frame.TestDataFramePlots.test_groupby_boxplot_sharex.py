def test_groupby_boxplot_sharex(self):
    df = DataFrame({'a': [-1.43, -0.15, -3.7, -1.43, -0.14], 'b': [0.56, 0.84, 0.29, 0.56, 0.85], 'c': [0, 1, 2, 3, 1]}, index=[0, 1, 2, 3, 4])
    axes = df.groupby('c').boxplot()
    expected = [True, True, True, True]
    self._assert_xtickslabels_visibility(axes, expected)
    axes = df.groupby('c').boxplot(sharex=False)
    expected = [True, True, True, True]
    self._assert_xtickslabels_visibility(axes, expected)
    axes = df.groupby('c').boxplot(sharex=True)
    expected = [False, False, True, True]
    self._assert_xtickslabels_visibility(axes, expected)