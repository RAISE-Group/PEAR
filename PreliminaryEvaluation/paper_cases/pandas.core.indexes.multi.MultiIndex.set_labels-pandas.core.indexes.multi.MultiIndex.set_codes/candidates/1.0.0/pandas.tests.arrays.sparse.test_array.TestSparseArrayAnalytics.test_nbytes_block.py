def test_nbytes_block(self):
    arr = SparseArray([1, 2, 0, 0, 0], kind='block')
    result = arr.nbytes
    assert result == 24