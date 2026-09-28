def test_delete(self):
    ci = self.create_index()
    categories = ci.categories
    result = ci.delete(0)
    expected = CategoricalIndex(list('abbca'), categories=categories)
    tm.assert_index_equal(result, expected, exact=True)
    result = ci.delete(-1)
    expected = CategoricalIndex(list('aabbc'), categories=categories)
    tm.assert_index_equal(result, expected, exact=True)
    with pytest.raises((IndexError, ValueError)):
        ci.delete(10)