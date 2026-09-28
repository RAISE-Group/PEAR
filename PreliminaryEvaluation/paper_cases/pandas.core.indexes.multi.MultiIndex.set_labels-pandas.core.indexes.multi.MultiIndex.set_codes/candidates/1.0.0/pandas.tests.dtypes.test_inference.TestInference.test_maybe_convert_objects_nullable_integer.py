@pytest.mark.parametrize('exp', [IntegerArray(np.array([2, 0], dtype='i8'), np.array([False, True])), IntegerArray(np.array([2, 0], dtype='int64'), np.array([False, True]))])
def test_maybe_convert_objects_nullable_integer(self, exp):
    arr = np.array([2, np.NaN], dtype=object)
    result = lib.maybe_convert_objects(arr, convert_to_nullable_integer=1)
    tm.assert_extension_array_equal(result, exp)