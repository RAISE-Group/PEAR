def test_total_seconds(self, timedelta_index):
    tdi = timedelta_index
    arr = TimedeltaArray(tdi)
    expected = tdi.total_seconds()
    result = arr.total_seconds()
    tm.assert_numpy_array_equal(result, expected.values)