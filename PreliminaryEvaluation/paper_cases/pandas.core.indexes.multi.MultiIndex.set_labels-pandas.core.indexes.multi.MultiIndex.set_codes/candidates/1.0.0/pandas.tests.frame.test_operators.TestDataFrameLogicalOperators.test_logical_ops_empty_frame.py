def test_logical_ops_empty_frame(self):
    df = DataFrame(index=[1])
    result = df & df
    tm.assert_frame_equal(result, df)
    result = df | df
    tm.assert_frame_equal(result, df)
    df2 = DataFrame(index=[1, 2])
    result = df & df2
    tm.assert_frame_equal(result, df2)
    dfa = DataFrame(index=[1], columns=['A'])
    result = dfa & dfa
    expected = DataFrame(False, index=[1], columns=['A'])
    tm.assert_frame_equal(result, expected)