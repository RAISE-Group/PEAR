def test_constructor_tuples(self):
    values = np.array([(1,), (1, 2), (1,), (1, 2)], dtype=object)
    result = Categorical(values)
    expected = Index([(1,), (1, 2)], tupleize_cols=False)
    tm.assert_index_equal(result.categories, expected)
    assert result.ordered is False