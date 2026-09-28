def test_reorder_categories(self):
    cat = Categorical(['a', 'b', 'c', 'a'], ordered=True)
    old = cat.copy()
    new = Categorical(['a', 'b', 'c', 'a'], categories=['c', 'b', 'a'], ordered=True)
    res = cat.reorder_categories(['c', 'b', 'a'])
    tm.assert_categorical_equal(cat, old)
    tm.assert_categorical_equal(res, new)
    res = cat.reorder_categories(['c', 'b', 'a'], inplace=True)
    assert res is None
    tm.assert_categorical_equal(cat, new)