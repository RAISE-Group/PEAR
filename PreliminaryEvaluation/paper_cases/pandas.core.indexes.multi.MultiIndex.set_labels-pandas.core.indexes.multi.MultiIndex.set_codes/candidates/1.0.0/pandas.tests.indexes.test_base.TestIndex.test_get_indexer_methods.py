@pytest.mark.parametrize('reverse', [True, False])
@pytest.mark.parametrize('expected,method', [(np.array([-1, 0, 0, 1, 1], dtype=np.intp), 'pad'), (np.array([-1, 0, 0, 1, 1], dtype=np.intp), 'ffill'), (np.array([0, 0, 1, 1, 2], dtype=np.intp), 'backfill'), (np.array([0, 0, 1, 1, 2], dtype=np.intp), 'bfill')])
def test_get_indexer_methods(self, reverse, expected, method):
    index1 = Index([1, 2, 3, 4, 5])
    index2 = Index([2, 4, 6])
    if reverse:
        index1 = index1[::-1]
        expected = expected[::-1]
    result = index2.get_indexer(index1, method=method)
    tm.assert_almost_equal(result, expected)