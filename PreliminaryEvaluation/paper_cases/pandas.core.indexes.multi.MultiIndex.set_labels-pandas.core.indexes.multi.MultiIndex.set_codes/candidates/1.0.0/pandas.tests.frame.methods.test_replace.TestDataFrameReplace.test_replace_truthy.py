def test_replace_truthy(self):
    df = DataFrame({'a': [True, True]})
    r = df.replace([np.inf, -np.inf], np.nan)
    e = df
    tm.assert_frame_equal(r, e)