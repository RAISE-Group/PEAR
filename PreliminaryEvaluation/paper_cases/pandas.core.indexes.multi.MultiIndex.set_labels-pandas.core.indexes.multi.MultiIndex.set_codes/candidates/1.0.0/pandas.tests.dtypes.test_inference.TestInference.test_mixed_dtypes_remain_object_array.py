def test_mixed_dtypes_remain_object_array(self):
    array = np.array([datetime(2015, 1, 1, tzinfo=pytz.utc), 1], dtype=object)
    result = lib.maybe_convert_objects(array, convert_datetime=1)
    tm.assert_numpy_array_equal(result, array)