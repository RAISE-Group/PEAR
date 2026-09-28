@pytest.mark.parametrize('skipna', [True, False])
def test_complex(self, skipna):
    arr = np.array([1.0, 2.0, 1 + 1j])
    result = lib.infer_dtype(arr, skipna=skipna)
    assert result == 'complex'
    arr = np.array([1.0, 2.0, 1 + 1j], dtype='O')
    result = lib.infer_dtype(arr, skipna=skipna)
    assert result == 'mixed'
    arr = np.array([1, np.nan, 1 + 1j])
    result = lib.infer_dtype(arr, skipna=skipna)
    assert result == 'complex'
    arr = np.array([1.0, np.nan, 1 + 1j], dtype='O')
    result = lib.infer_dtype(arr, skipna=skipna)
    assert result == 'mixed'
    arr = np.array([1 + 1j, np.nan, 3 + 3j], dtype='O')
    result = lib.infer_dtype(arr, skipna=skipna)
    assert result == 'complex'
    arr = np.array([1 + 1j, np.nan, 3 + 3j], dtype=np.complex64)
    result = lib.infer_dtype(arr, skipna=skipna)
    assert result == 'complex'