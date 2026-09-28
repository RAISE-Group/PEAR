def test_bounds_check_large(self):
    arr = np.array([1, 2])
    with pytest.raises(IndexError):
        algos.take(arr, [2, 3], allow_fill=True)
    with pytest.raises(IndexError):
        algos.take(arr, [2, 3], allow_fill=False)