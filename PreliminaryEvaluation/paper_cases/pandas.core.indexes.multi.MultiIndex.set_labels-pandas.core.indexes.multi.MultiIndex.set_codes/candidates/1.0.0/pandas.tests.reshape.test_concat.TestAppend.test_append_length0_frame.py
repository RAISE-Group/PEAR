def test_append_length0_frame(self, sort):
    df = DataFrame(columns=['A', 'B', 'C'])
    df3 = DataFrame(index=[0, 1], columns=['A', 'B'])
    df5 = df.append(df3, sort=sort)
    expected = DataFrame(index=[0, 1], columns=['A', 'B', 'C'])
    tm.assert_frame_equal(df5, expected)