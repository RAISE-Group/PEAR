@pytest.mark.parametrize('arr, skipna', [(np.array([1, 2, np.nan, np.nan, 3], dtype='O'), False), (np.array([1, 2, np.nan, np.nan, 3], dtype='O'), True), (np.array([1, 2, 3, np.int64(4), np.int32(5), np.nan], dtype='O'), False), (np.array([1, 2, 3, np.int64(4), np.int32(5), np.nan], dtype='O'), True)])
def test_integer_na(self, arr, skipna):
    result = lib.infer_dtype(arr, skipna=skipna)
    expected = 'integer' if skipna else 'integer-na'
    assert result == expected