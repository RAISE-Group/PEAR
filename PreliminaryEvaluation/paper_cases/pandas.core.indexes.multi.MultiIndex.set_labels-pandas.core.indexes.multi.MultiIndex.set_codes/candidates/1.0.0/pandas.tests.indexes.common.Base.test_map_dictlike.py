@pytest.mark.parametrize('mapper', [lambda values, index: {i: e for e, i in zip(values, index)}, lambda values, index: pd.Series(values, index)])
def test_map_dictlike(self, mapper):
    index = self.create_index()
    if isinstance(index, (pd.CategoricalIndex, pd.IntervalIndex)):
        pytest.skip('skipping tests for {}'.format(type(index)))
    identity = mapper(index.values, index)
    if isinstance(index, pd.UInt64Index) and isinstance(identity, dict):
        expected = index.astype('int64')
    else:
        expected = index
    result = index.map(identity)
    tm.assert_index_equal(result, expected)
    expected = pd.Index([np.nan] * len(index))
    result = index.map(mapper(expected, index))
    tm.assert_index_equal(result, expected)