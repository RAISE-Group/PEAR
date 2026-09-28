@td.xfail_non_writeable
@pytest.mark.parametrize('compression', [False, pytest.param(True, marks=td.skip_if_windows_python_3)])
def test_store_mixed(self, compression, setup_path):

    def _make_one():
        df = tm.makeDataFrame()
        df['obj1'] = 'foo'
        df['obj2'] = 'bar'
        df['bool1'] = df['A'] > 0
        df['bool2'] = df['B'] > 0
        df['int1'] = 1
        df['int2'] = 2
        return df._consolidate()
    df1 = _make_one()
    df2 = _make_one()
    self._check_roundtrip(df1, tm.assert_frame_equal, path=setup_path)
    self._check_roundtrip(df2, tm.assert_frame_equal, path=setup_path)
    with ensure_clean_store(setup_path) as store:
        store['obj'] = df1
        tm.assert_frame_equal(store['obj'], df1)
        store['obj'] = df2
        tm.assert_frame_equal(store['obj'], df2)
    self._check_roundtrip(df1['obj1'], tm.assert_series_equal, path=setup_path, compression=compression)
    self._check_roundtrip(df1['bool1'], tm.assert_series_equal, path=setup_path, compression=compression)
    self._check_roundtrip(df1['int1'], tm.assert_series_equal, path=setup_path, compression=compression)