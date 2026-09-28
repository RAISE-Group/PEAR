def test_boolean_selection(self):
    df3 = self.df3
    df4 = self.df4
    result = df3[df3.index == 'a']
    expected = df3.iloc[[]]
    tm.assert_frame_equal(result, expected)
    result = df4[df4.index == 'a']
    expected = df4.iloc[[]]
    tm.assert_frame_equal(result, expected)
    result = df3[df3.index == 1]
    expected = df3.iloc[[0, 1, 3]]
    tm.assert_frame_equal(result, expected)
    result = df4[df4.index == 1]
    expected = df4.iloc[[0, 1, 3]]
    tm.assert_frame_equal(result, expected)
    result = df3[df3.index < 2]
    expected = df3.iloc[[4]]
    tm.assert_frame_equal(result, expected)
    result = df3[df3.index > 1]
    expected = df3.iloc[[]]
    tm.assert_frame_equal(result, expected)
    msg = 'Unordered Categoricals can only compare equality or not'
    with pytest.raises(TypeError, match=msg):
        df4[df4.index < 2]
    with pytest.raises(TypeError, match=msg):
        df4[df4.index > 1]