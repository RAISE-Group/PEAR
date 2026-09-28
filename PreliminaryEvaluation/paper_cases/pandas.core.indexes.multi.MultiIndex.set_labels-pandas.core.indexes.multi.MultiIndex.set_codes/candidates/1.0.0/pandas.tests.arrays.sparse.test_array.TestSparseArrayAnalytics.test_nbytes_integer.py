def test_nbytes_integer(self):
    arr = SparseArray([1, 0, 0, 0, 2], kind='integer')
    result = arr.nbytes
    assert result == 24