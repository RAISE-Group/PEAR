def test_lots_of_operators_string(self, df):
    res = df.query("`  &^ :!€$?(} >    <++*''  ` > 4")
    expect = df[df["  &^ :!€$?(} >    <++*''  "] > 4]
    tm.assert_frame_equal(res, expect)