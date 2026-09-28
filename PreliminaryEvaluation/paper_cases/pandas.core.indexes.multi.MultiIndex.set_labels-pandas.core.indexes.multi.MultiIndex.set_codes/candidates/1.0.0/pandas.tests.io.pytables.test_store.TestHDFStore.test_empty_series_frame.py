@td.xfail_non_writeable
def test_empty_series_frame(self, setup_path):
    s0 = Series(dtype=object)
    s1 = Series(name='myseries', dtype=object)
    df0 = DataFrame()
    df1 = DataFrame(index=['a', 'b', 'c'])
    df2 = DataFrame(columns=['d', 'e', 'f'])
    self._check_roundtrip(s0, tm.assert_series_equal, path=setup_path)
    self._check_roundtrip(s1, tm.assert_series_equal, path=setup_path)
    self._check_roundtrip(df0, tm.assert_frame_equal, path=setup_path)
    self._check_roundtrip(df1, tm.assert_frame_equal, path=setup_path)
    self._check_roundtrip(df2, tm.assert_frame_equal, path=setup_path)