def test_replace_pure_bool_with_string_no_op(self):
    df = DataFrame(np.random.rand(2, 2) > 0.5)
    result = df.replace('asdf', 'fdsa')
    tm.assert_frame_equal(df, result)