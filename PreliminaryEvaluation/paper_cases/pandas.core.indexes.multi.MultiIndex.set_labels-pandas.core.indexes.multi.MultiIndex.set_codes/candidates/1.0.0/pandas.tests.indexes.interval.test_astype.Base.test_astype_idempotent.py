def test_astype_idempotent(self, index):
    result = index.astype('interval')
    tm.assert_index_equal(result, index)
    result = index.astype(index.dtype)
    tm.assert_index_equal(result, index)