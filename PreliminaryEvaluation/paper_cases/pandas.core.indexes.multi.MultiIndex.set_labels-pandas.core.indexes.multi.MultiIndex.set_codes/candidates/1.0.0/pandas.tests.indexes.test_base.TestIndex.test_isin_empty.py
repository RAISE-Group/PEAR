@pytest.mark.parametrize('empty', [[], Series(dtype=object), np.array([])])
def test_isin_empty(self, empty):
    index = Index(['a', 'b'])
    expected = np.array([False, False])
    result = index.isin(empty)
    tm.assert_numpy_array_equal(expected, result)