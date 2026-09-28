@pytest.mark.parametrize('data, names, expected', [([[1, 2, 3]], None, Index([1, 2, 3])), ([[1, 2, 3]], ['name'], Index([1, 2, 3], name='name')), ([['a', 'a'], ['c', 'd']], None, MultiIndex([['a'], ['c', 'd']], [[0, 0], [0, 1]])), ([['a', 'a'], ['c', 'd']], ['L1', 'L2'], MultiIndex([['a'], ['c', 'd']], [[0, 0], [0, 1]], names=['L1', 'L2']))])
def test_ensure_index_from_sequences(self, data, names, expected):
    result = ensure_index_from_sequences(data, names)
    tm.assert_index_equal(result, expected)