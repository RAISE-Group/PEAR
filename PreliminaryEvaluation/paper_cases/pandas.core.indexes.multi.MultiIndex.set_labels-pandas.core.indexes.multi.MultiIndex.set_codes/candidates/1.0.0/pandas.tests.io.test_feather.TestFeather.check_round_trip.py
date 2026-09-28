def check_round_trip(self, df, expected=None, **kwargs):
    if expected is None:
        expected = df
    with tm.ensure_clean() as path:
        to_feather(df, path)
        result = read_feather(path, **kwargs)
        tm.assert_frame_equal(result, expected)