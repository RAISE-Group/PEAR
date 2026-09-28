def test_partial_set_empty_frame_empty_copy_assignment(self):
    df = DataFrame(index=[0])
    df = df.copy()
    df['a'] = 0
    expected = DataFrame(0, index=[0], columns=['a'])
    tm.assert_frame_equal(df, expected)