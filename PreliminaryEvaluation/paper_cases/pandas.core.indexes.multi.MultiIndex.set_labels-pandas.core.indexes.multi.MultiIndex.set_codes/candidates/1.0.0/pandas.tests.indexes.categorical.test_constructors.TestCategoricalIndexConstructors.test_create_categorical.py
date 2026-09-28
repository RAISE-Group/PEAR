def test_create_categorical(self):
    ci = CategoricalIndex(['a', 'b', 'c'])
    result = CategoricalIndex._create_categorical(ci, ci)
    expected = Categorical(['a', 'b', 'c'])
    tm.assert_categorical_equal(result, expected)