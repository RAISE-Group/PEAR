def test_update_dtype_string(self, ordered_fixture):
    dtype = CategoricalDtype(list('abc'), ordered_fixture)
    expected_categories = dtype.categories
    expected_ordered = dtype.ordered
    result = dtype.update_dtype('category')
    tm.assert_index_equal(result.categories, expected_categories)
    assert result.ordered is expected_ordered