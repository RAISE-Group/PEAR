def test_getitem_category_type(self):
    s = Series([1, 2, 3]).astype('category')
    result = s.iloc[0:2]
    expected = Series([1, 2]).astype(CategoricalDtype([1, 2, 3]))
    tm.assert_series_equal(result, expected)
    result = s.iloc[[0, 1]]
    expected = Series([1, 2]).astype(CategoricalDtype([1, 2, 3]))
    tm.assert_series_equal(result, expected)
    result = s.iloc[[True, False, False]]
    expected = Series([1]).astype(CategoricalDtype([1, 2, 3]))
    tm.assert_series_equal(result, expected)