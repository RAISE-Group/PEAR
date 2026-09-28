@pytest.mark.parametrize('allow_fill', [True, False])
def test_take_empty(self, allow_fill):
    arr = np.array([], dtype=np.int64)
    result = algos.take(arr, [], allow_fill=allow_fill)
    tm.assert_numpy_array_equal(arr, result)
    with pytest.raises(IndexError):
        algos.take(arr, [0], allow_fill=allow_fill)