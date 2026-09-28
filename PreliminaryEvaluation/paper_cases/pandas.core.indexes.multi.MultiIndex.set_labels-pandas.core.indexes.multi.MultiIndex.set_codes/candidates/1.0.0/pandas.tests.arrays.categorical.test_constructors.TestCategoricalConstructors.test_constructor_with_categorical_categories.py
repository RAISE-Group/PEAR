def test_constructor_with_categorical_categories(self):
    expected = Categorical(['a', 'b'], categories=['a', 'b', 'c'])
    result = Categorical(['a', 'b'], categories=Categorical(['a', 'b', 'c']))
    tm.assert_categorical_equal(result, expected)
    result = Categorical(['a', 'b'], categories=CategoricalIndex(['a', 'b', 'c']))
    tm.assert_categorical_equal(result, expected)