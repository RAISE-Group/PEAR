def test_from_dtype(self, data):
    dtype = data.dtype
    expected = pd.Series(data)
    result = pd.Series(list(data), dtype=dtype)
    self.assert_series_equal(result, expected)
    result = pd.Series(list(data), dtype=str(dtype))
    self.assert_series_equal(result, expected)
    expected = pd.DataFrame(data).astype(dtype)
    result = pd.DataFrame(list(data), dtype=dtype)
    self.assert_frame_equal(result, expected)
    result = pd.DataFrame(list(data), dtype=str(dtype))
    self.assert_frame_equal(result, expected)