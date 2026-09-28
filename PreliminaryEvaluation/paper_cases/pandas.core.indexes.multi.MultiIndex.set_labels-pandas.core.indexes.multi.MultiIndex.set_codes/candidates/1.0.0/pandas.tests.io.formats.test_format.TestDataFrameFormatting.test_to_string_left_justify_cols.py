def test_to_string_left_justify_cols(self):
    tm.reset_display_options()
    df = DataFrame({'x': [3234, 0.253]})
    df_s = df.to_string(justify='left')
    expected = '   x       \n0  3234.000\n1     0.253'
    assert df_s == expected