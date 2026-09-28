@pytest.mark.parametrize('empty', [[], Series(dtype=object), np.array([])])
def test_empty(self, empty):
    vals = Index(['a', 'b'])
    expected = np.array([False, False])
    result = algos.isin(vals, empty)
    tm.assert_numpy_array_equal(expected, result)