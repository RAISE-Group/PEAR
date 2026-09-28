def test_indexing_assignment_dict_already_exists(self):
    df = DataFrame({'x': [1, 2, 6], 'y': [2, 2, 8], 'z': [-5, 0, 5]}).set_index('z')
    expected = df.copy()
    rhs = dict(x=9, y=99)
    df.loc[5] = rhs
    expected.loc[5] = [9, 99]
    tm.assert_frame_equal(df, expected)