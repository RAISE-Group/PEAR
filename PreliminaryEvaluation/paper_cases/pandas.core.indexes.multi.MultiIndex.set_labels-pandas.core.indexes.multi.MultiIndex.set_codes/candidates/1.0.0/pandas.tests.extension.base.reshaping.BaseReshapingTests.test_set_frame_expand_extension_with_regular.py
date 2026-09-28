def test_set_frame_expand_extension_with_regular(self, data):
    df = pd.DataFrame({'A': data})
    df['B'] = [1] * len(data)
    expected = pd.DataFrame({'A': data, 'B': [1] * len(data)})
    self.assert_frame_equal(df, expected)