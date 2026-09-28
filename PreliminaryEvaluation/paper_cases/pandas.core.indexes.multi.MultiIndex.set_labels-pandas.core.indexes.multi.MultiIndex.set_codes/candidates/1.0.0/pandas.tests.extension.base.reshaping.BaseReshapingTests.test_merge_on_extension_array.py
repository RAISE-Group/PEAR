def test_merge_on_extension_array(self, data):
    a, b = data[:2]
    key = type(data)._from_sequence([a, b], dtype=data.dtype)
    df = pd.DataFrame({'key': key, 'val': [1, 2]})
    result = pd.merge(df, df, on='key')
    expected = pd.DataFrame({'key': key, 'val_x': [1, 2], 'val_y': [1, 2]})
    self.assert_frame_equal(result, expected)
    result = pd.merge(df.iloc[[1, 0]], df, on='key')
    expected = expected.iloc[[1, 0]].reset_index(drop=True)
    self.assert_frame_equal(result, expected)