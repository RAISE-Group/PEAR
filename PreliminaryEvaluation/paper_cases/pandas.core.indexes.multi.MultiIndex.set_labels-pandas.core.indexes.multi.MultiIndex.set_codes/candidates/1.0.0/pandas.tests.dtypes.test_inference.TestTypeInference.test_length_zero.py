@pytest.mark.parametrize('skipna', [True, False])
def test_length_zero(self, skipna):
    result = lib.infer_dtype(np.array([], dtype='i4'), skipna=skipna)
    assert result == 'integer'
    result = lib.infer_dtype([], skipna=skipna)
    assert result == 'empty'
    arr = np.array([np.array([], dtype=object), np.array([], dtype=object)])
    result = lib.infer_dtype(arr, skipna=skipna)
    assert result == 'empty'