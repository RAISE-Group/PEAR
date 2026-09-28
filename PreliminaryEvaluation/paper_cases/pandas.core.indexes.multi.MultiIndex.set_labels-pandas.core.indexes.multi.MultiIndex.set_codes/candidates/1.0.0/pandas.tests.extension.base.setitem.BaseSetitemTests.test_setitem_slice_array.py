def test_setitem_slice_array(self, data):
    arr = data[:5].copy()
    arr[:5] = data[-5:]
    self.assert_extension_array_equal(arr, data[-5:])