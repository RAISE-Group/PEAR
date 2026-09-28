def test_union_categorical_same_categories_different_order(self):
    c1 = Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c'])
    c2 = Categorical(['a', 'b', 'c'], categories=['b', 'a', 'c'])
    result = union_categoricals([c1, c2])
    expected = Categorical(['a', 'b', 'c', 'a', 'b', 'c'], categories=['a', 'b', 'c'])
    tm.assert_categorical_equal(result, expected)