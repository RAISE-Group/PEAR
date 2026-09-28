def test_partial_setting_mixed_dtype(self):
    df = DataFrame([[True, 1], [False, 2]], columns=['female', 'fitness'])
    s = df.loc[1].copy()
    s.name = 2
    expected = df.append(s)
    df.loc[2] = df.loc[1]
    tm.assert_frame_equal(df, expected)
    df = DataFrame(columns=['A', 'B'])
    df.loc[0] = Series(1, index=range(4))
    tm.assert_frame_equal(df, DataFrame(columns=['A', 'B'], index=[0]))
    df = DataFrame(columns=['A', 'B'])
    df.loc[0] = Series(1, index=['B'])
    exp = DataFrame([[np.nan, 1]], columns=['A', 'B'], index=[0], dtype='float64')
    tm.assert_frame_equal(df, exp)
    df = DataFrame(columns=['A', 'B'])
    with pytest.raises(ValueError):
        df.loc[0] = [1, 2, 3]
    df = DataFrame(columns=['A', 'B'])
    df.loc[3] = [6, 7]
    exp = DataFrame([[6, 7]], index=[3], columns=['A', 'B'], dtype='object')
    tm.assert_frame_equal(df, exp)