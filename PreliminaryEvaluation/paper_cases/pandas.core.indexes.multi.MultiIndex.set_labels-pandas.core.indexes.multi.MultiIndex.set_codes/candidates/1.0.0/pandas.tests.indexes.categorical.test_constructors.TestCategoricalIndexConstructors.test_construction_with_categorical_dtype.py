def test_construction_with_categorical_dtype(self):
    data, cats, ordered = ('a a b b'.split(), 'c b a'.split(), True)
    dtype = CategoricalDtype(categories=cats, ordered=ordered)
    result = CategoricalIndex(data, dtype=dtype)
    expected = CategoricalIndex(data, categories=cats, ordered=ordered)
    tm.assert_index_equal(result, expected, exact=True)
    result = Index(data, dtype=dtype)
    tm.assert_index_equal(result, expected, exact=True)
    msg = 'Cannot specify `categories` or `ordered` together with `dtype`.'
    with pytest.raises(ValueError, match=msg):
        CategoricalIndex(data, categories=cats, dtype=dtype)
    with pytest.raises(ValueError, match=msg):
        Index(data, categories=cats, dtype=dtype)
    with pytest.raises(ValueError, match=msg):
        CategoricalIndex(data, ordered=ordered, dtype=dtype)
    with pytest.raises(ValueError, match=msg):
        Index(data, ordered=ordered, dtype=dtype)