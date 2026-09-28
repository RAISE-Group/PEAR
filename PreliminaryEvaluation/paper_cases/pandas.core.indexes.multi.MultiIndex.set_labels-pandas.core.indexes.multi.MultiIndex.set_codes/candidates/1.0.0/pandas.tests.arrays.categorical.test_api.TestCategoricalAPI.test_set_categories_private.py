def test_set_categories_private(self):
    cat = Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c', 'd'])
    cat._set_categories(['a', 'c', 'd', 'e'])
    expected = Categorical(['a', 'c', 'd'], categories=list('acde'))
    tm.assert_categorical_equal(cat, expected)
    cat = Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c', 'd'])
    cat._set_categories(['a', 'c', 'd', 'e'], fastpath=True)
    expected = Categorical(['a', 'c', 'd'], categories=list('acde'))
    tm.assert_categorical_equal(cat, expected)