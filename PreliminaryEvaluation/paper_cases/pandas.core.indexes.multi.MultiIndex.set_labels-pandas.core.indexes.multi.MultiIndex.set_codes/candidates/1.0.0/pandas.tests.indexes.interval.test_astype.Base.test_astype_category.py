def test_astype_category(self, index):
    result = index.astype('category')
    expected = CategoricalIndex(index.values)
    tm.assert_index_equal(result, expected)
    result = index.astype(CategoricalDtype())
    tm.assert_index_equal(result, expected)
    categories = index.dropna().unique().values[:-1]
    dtype = CategoricalDtype(categories=categories, ordered=True)
    result = index.astype(dtype)
    expected = CategoricalIndex(index.values, categories=categories, ordered=True)
    tm.assert_index_equal(result, expected)