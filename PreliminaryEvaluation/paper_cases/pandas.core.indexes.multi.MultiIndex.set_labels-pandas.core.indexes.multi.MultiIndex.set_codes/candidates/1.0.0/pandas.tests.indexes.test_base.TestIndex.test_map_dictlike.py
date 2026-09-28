@pytest.mark.parametrize('mapper', [lambda values, index: {i: e for e, i in zip(values, index)}, lambda values, index: pd.Series(values, index)])
def test_map_dictlike(self, indices, mapper):
    if isinstance(indices, CategoricalIndex):
        return
    elif not indices.is_unique:
        return
    if indices.empty:
        expected = Index([])
    else:
        expected = Index(np.arange(len(indices), 0, -1))
    result = indices.map(mapper(expected, indices))
    tm.assert_index_equal(result, expected)