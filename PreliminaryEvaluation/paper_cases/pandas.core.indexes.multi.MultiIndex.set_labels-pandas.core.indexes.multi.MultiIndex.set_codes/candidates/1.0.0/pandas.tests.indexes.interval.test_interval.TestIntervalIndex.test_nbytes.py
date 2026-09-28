def test_nbytes(self):
    left = np.arange(0, 4, dtype='i8')
    right = np.arange(1, 5, dtype='i8')
    result = IntervalIndex.from_arrays(left, right).nbytes
    expected = 64
    assert result == expected