def test_shift_categorical(self):
    s1 = pd.Series(['a', 'b', 'c'], dtype='category')
    s2 = pd.Series(['A', 'B', 'C'], dtype='category')
    df = DataFrame({'one': s1, 'two': s2})
    rs = df.shift(1)
    xp = DataFrame({'one': s1.shift(1), 'two': s2.shift(1)})
    tm.assert_frame_equal(rs, xp)