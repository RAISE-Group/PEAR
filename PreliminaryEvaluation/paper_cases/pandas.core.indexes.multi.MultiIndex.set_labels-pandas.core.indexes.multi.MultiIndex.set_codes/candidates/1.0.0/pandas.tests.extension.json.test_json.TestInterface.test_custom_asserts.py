def test_custom_asserts(self):
    data = JSONArray([collections.UserDict({'a': 1}), collections.UserDict({'b': 2}), collections.UserDict({'c': 3})])
    a = pd.Series(data)
    self.assert_series_equal(a, a)
    self.assert_frame_equal(a.to_frame(), a.to_frame())
    b = pd.Series(data.take([0, 0, 1]))
    with pytest.raises(AssertionError):
        self.assert_series_equal(a, b)
    with pytest.raises(AssertionError):
        self.assert_frame_equal(a.to_frame(), b.to_frame())