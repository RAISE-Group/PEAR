@pytest.mark.parametrize('shape', [(10, 10), (5, 5, 4), (100, 1)])
def test_array_reshaped(self, shape):
    arr = np.arange(100)
    arr = arr.reshape(shape)
    tm.assert_numpy_array_equal(np.array(ujson.decode(ujson.encode(arr))), arr)
    tm.assert_numpy_array_equal(ujson.decode(ujson.encode(arr), numpy=True), arr)