def test_set_frame_expand_regular_with_extension(self, data):
    df = pd.DataFrame({'A': [1] * len(data)})
    df['B'] = data
    expected = pd.DataFrame({'A': [1] * len(data), 'B': data})
    self.assert_frame_equal(df, expected)