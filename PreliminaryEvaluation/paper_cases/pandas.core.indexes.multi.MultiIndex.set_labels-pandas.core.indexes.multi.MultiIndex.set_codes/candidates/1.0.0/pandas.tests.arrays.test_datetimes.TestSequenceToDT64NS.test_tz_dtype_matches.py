def test_tz_dtype_matches(self):
    arr = DatetimeArray._from_sequence(['2000'], tz='US/Central')
    result, _, _ = sequence_to_dt64ns(arr, dtype=DatetimeTZDtype(tz='US/Central'))
    tm.assert_numpy_array_equal(arr._data, result)