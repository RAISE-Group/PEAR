@pytest.mark.parametrize('mapper', [lambda values, index: {i: e for e, i in zip(values, index)}, lambda values, index: pd.Series(values, index)])
def test_map_dictlike_simple(self, mapper):
    expected = Index(['foo', 'bar', 'baz'])
    index = tm.makeIntIndex(3)
    result = index.map(mapper(expected.values, index))
    tm.assert_index_equal(result, expected)