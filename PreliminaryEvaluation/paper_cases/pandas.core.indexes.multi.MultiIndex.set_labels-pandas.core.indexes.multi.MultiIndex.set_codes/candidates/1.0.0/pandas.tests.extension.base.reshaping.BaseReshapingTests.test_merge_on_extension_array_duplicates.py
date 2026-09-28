def test_merge_on_extension_array_duplicates(self, data):
    a, b = data[:2]
    key = type(data)._from_sequence([a, b, a], dtype=data.dtype)
    df1 = pd.DataFrame({'key': key, 'val': [1, 2, 3]})
    df2 = pd.DataFrame({'key': key, 'val': [1, 2, 3]})
    result = pd.merge(df1, df2, on='key')
    expected = pd.DataFrame({'key': key.take([0, 0, 0, 0, 1]), 'val_x': [1, 1, 3, 3, 2], 'val_y': [1, 3, 1, 3, 2]})
    self.assert_frame_equal(result, expected)