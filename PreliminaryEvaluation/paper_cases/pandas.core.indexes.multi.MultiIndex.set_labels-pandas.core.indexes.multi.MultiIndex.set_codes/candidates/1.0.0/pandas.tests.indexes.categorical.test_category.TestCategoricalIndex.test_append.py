def test_append(self):
    ci = self.create_index()
    categories = ci.categories
    result = ci[:3].append(ci[3:])
    tm.assert_index_equal(result, ci, exact=True)
    foos = [ci[:1], ci[1:3], ci[3:]]
    result = foos[0].append(foos[1:])
    tm.assert_index_equal(result, ci, exact=True)
    result = ci.append([])
    tm.assert_index_equal(result, ci, exact=True)
    msg = 'all inputs must be Index'
    with pytest.raises(TypeError, match=msg):
        ci.append(ci.values.set_categories(list('abcd')))
    with pytest.raises(TypeError, match=msg):
        ci.append(ci.values.reorder_categories(list('abc')))
    result = ci.append(Index(['c', 'a']))
    expected = CategoricalIndex(list('aabbcaca'), categories=categories)
    tm.assert_index_equal(result, expected, exact=True)
    msg = 'cannot append a non-category item to a CategoricalIndex'
    with pytest.raises(TypeError, match=msg):
        ci.append(Index(['a', 'd']))
    result = Index(['c', 'a']).append(ci)
    expected = Index(list('caaabbca'))
    tm.assert_index_equal(result, expected, exact=True)