def test_from_codes_with_categorical_categories(self):
    expected = Categorical(['a', 'b'], categories=['a', 'b', 'c'])
    result = Categorical.from_codes([0, 1], categories=Categorical(['a', 'b', 'c']))
    tm.assert_categorical_equal(result, expected)
    result = Categorical.from_codes([0, 1], categories=CategoricalIndex(['a', 'b', 'c']))
    tm.assert_categorical_equal(result, expected)
    with pytest.raises(ValueError, match='Categorical categories must be unique'):
        Categorical.from_codes([0, 1], Categorical(['a', 'b', 'a']))