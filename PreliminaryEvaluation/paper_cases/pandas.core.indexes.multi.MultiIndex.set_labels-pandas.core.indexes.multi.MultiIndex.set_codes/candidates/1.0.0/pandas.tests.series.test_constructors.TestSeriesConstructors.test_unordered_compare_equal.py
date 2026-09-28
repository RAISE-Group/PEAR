def test_unordered_compare_equal(self):
    left = pd.Series(['a', 'b', 'c'], dtype=CategoricalDtype(['a', 'b']))
    right = pd.Series(pd.Categorical(['a', 'b', np.nan], categories=['a', 'b']))
    tm.assert_series_equal(left, right)