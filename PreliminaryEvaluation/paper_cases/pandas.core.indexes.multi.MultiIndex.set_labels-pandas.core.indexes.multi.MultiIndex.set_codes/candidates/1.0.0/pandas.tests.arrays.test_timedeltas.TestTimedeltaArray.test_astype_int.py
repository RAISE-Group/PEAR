@pytest.mark.parametrize('dtype', [int, np.int32, np.int64, 'uint32', 'uint64'])
def test_astype_int(self, dtype):
    arr = TimedeltaArray._from_sequence([pd.Timedelta('1H'), pd.Timedelta('2H')])
    result = arr.astype(dtype)
    if np.dtype(dtype).kind == 'u':
        expected_dtype = np.dtype('uint64')
    else:
        expected_dtype = np.dtype('int64')
    expected = arr.astype(expected_dtype)
    assert result.dtype == expected_dtype
    tm.assert_numpy_array_equal(result, expected)