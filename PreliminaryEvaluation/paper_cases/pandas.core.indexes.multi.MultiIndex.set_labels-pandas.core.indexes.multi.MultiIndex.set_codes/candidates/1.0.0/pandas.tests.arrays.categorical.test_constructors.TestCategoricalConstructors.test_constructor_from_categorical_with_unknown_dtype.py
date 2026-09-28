def test_constructor_from_categorical_with_unknown_dtype(self):
    dtype = CategoricalDtype(None, ordered=True)
    values = Categorical(['a', 'b', 'd'])
    result = Categorical(values, dtype=dtype)
    expected = Categorical(['a', 'b', 'd'], categories=['a', 'b', 'd'], ordered=True)
    tm.assert_categorical_equal(result, expected)