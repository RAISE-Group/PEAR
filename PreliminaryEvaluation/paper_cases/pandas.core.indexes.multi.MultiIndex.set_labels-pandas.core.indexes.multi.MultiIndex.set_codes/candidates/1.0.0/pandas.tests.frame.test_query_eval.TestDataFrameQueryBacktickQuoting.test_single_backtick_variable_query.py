def test_single_backtick_variable_query(self, df):
    res = df.query('1 < `B B`')
    expect = df[1 < df['B B']]
    tm.assert_frame_equal(res, expect)