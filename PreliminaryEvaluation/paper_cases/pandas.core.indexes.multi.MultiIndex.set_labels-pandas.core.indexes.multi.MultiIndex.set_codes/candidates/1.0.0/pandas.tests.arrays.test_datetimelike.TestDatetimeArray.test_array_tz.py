def test_array_tz(self, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = pd.date_range('2016-01-01', periods=3, tz=tz)
    arr = DatetimeArray(dti)
    expected = dti.asi8.view('M8[ns]')
    result = np.array(arr, dtype='M8[ns]')
    tm.assert_numpy_array_equal(result, expected)
    result = np.array(arr, dtype='datetime64[ns]')
    tm.assert_numpy_array_equal(result, expected)
    result = np.array(arr, dtype='M8[ns]', copy=False)
    assert result.base is expected.base
    assert result.base is not None
    result = np.array(arr, dtype='datetime64[ns]', copy=False)
    assert result.base is expected.base
    assert result.base is not None