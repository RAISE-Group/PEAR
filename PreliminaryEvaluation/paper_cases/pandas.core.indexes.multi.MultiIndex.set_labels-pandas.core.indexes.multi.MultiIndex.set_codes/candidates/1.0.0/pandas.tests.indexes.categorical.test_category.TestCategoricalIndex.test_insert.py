def test_insert(self):
    ci = self.create_index()
    categories = ci.categories
    result = ci.insert(0, 'a')
    expected = CategoricalIndex(list('aaabbca'), categories=categories)
    tm.assert_index_equal(result, expected, exact=True)
    result = ci.insert(-1, 'a')
    expected = CategoricalIndex(list('aabbcaa'), categories=categories)
    tm.assert_index_equal(result, expected, exact=True)
    result = CategoricalIndex(categories=categories).insert(0, 'a')
    expected = CategoricalIndex(['a'], categories=categories)
    tm.assert_index_equal(result, expected, exact=True)
    msg = 'cannot insert an item into a CategoricalIndex that is not already an existing category'
    with pytest.raises(TypeError, match=msg):
        ci.insert(0, 'd')
    expected = CategoricalIndex(['a', np.nan, 'a', 'b', 'c', 'b'])
    for na in (np.nan, pd.NaT, None):
        result = CategoricalIndex(list('aabcb')).insert(1, na)
        tm.assert_index_equal(result, expected)