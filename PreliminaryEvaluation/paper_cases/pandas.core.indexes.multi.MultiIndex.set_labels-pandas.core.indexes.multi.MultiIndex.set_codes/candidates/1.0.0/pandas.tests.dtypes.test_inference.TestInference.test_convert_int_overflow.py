@pytest.mark.parametrize('value', [-2 ** 63 - 1, 2 ** 64])
def test_convert_int_overflow(self, value):
    arr = np.array([value], dtype=object)
    result = lib.maybe_convert_objects(arr)
    tm.assert_numpy_array_equal(arr, result)