@pytest.mark.parametrize('kind', ['integer', 'block'])
def test_basic(self, kind):
    a = SparseArray([1, 0, 0, 2], kind=kind)
    b = SparseArray([1, 0, 2, 2], kind=kind)
    result = SparseArray._concat_same_type([a, b])
    expected = np.array([1, 2, 1, 2, 2], dtype='int64')
    tm.assert_numpy_array_equal(result.sp_values, expected)
    assert result.kind == kind