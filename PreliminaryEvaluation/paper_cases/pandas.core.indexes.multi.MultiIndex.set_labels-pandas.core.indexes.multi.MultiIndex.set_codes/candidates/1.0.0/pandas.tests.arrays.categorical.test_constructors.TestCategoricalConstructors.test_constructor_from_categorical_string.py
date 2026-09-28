def test_constructor_from_categorical_string(self):
    values = Categorical(['a', 'b', 'd'])
    result = Categorical(values, categories=['a', 'b', 'c'], ordered=True, dtype='category')
    expected = Categorical(['a', 'b', 'd'], categories=['a', 'b', 'c'], ordered=True)
    tm.assert_categorical_equal(result, expected)
    result = Categorical(values, categories=['a', 'b', 'c'], ordered=True)
    tm.assert_categorical_equal(result, expected)