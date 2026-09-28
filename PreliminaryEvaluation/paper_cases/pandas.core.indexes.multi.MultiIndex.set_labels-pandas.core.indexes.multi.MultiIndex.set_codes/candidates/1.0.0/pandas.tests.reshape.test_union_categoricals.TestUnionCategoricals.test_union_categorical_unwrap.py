def test_union_categorical_unwrap(self):
    c1 = Categorical(['a', 'b'])
    c2 = pd.Series(['b', 'c'], dtype='category')
    result = union_categoricals([c1, c2])
    expected = Categorical(['a', 'b', 'b', 'c'])
    tm.assert_categorical_equal(result, expected)
    c2 = CategoricalIndex(c2)
    result = union_categoricals([c1, c2])
    tm.assert_categorical_equal(result, expected)
    c1 = Series(c1)
    result = union_categoricals([c1, c2])
    tm.assert_categorical_equal(result, expected)
    with pytest.raises(TypeError):
        union_categoricals([c1, ['a', 'b', 'c']])