def test_array_object_dtype(self, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = pd.date_range('2016-01-01', periods=3, tz=tz)
    arr = DatetimeArray(dti)
    expected = np.array(list(dti))
    result = np.array(arr, dtype=object)
    tm.assert_numpy_array_equal(result, expected)
    result = np.array(dti, dtype=object)
    tm.assert_numpy_array_equal(result, expected)