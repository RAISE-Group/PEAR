def test_concat_extension_arrays_copy_false(self, data, na_value):
    df1 = pd.DataFrame({'A': data[:3]})
    df2 = pd.DataFrame({'B': data[3:7]})
    expected = pd.DataFrame({'A': data._from_sequence(list(data[:3]) + [na_value], dtype=data.dtype), 'B': data[3:7]})
    result = pd.concat([df1, df2], axis=1, copy=False)
    self.assert_frame_equal(result, expected)