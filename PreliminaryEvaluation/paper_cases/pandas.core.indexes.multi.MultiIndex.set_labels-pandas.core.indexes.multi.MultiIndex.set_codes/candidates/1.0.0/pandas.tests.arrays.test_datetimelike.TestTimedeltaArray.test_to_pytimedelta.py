def test_to_pytimedelta(self, timedelta_index):
    tdi = timedelta_index
    arr = TimedeltaArray(tdi)
    expected = tdi.to_pytimedelta()
    result = arr.to_pytimedelta()
    tm.assert_numpy_array_equal(result, expected)