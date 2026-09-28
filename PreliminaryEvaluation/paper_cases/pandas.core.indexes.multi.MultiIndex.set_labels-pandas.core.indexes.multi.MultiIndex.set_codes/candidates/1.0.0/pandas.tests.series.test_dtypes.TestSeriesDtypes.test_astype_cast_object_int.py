def test_astype_cast_object_int(self):
    arr = Series(['1', '2', '3', '4'], dtype=object)
    result = arr.astype(int)
    tm.assert_series_equal(result, Series(np.arange(1, 5)))