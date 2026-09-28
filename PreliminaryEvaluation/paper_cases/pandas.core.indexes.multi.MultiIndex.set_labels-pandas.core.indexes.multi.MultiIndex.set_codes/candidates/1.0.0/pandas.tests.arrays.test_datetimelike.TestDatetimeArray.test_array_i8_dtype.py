def test_array_i8_dtype(self, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = pd.date_range('2016-01-01', periods=3, tz=tz)
    arr = DatetimeArray(dti)
    expected = dti.asi8
    result = np.array(arr, dtype='i8')
    tm.assert_numpy_array_equal(result, expected)
    result = np.array(arr, dtype=np.int64)
    tm.assert_numpy_array_equal(result, expected)
    result = np.array(arr, dtype='i8', copy=False)
    assert result.base is not expected.base
    assert result.base is None