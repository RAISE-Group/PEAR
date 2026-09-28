@td.xfail_non_writeable
def test_store_datetime_mixed(self, setup_path):
    df = DataFrame({'a': [1, 2, 3], 'b': [1.0, 2.0, 3.0], 'c': ['a', 'b', 'c']})
    ts = tm.makeTimeSeries()
    df['d'] = ts.index[:3]
    self._check_roundtrip(df, tm.assert_frame_equal, path=setup_path)