@td.xfail_non_writeable
@pytest.mark.parametrize('compression', [False, pytest.param(True, marks=td.skip_if_windows_python_3)])
def test_frame(self, compression, setup_path):
    df = tm.makeDataFrame()
    df.values[0, 0] = np.nan
    df.values[5, 3] = np.nan
    self._check_roundtrip_table(df, tm.assert_frame_equal, path=setup_path, compression=compression)
    self._check_roundtrip(df, tm.assert_frame_equal, path=setup_path, compression=compression)
    tdf = tm.makeTimeDataFrame()
    self._check_roundtrip(tdf, tm.assert_frame_equal, path=setup_path, compression=compression)
    with ensure_clean_store(setup_path) as store:
        df['foo'] = np.random.randn(len(df))
        store['df'] = df
        recons = store['df']
        assert recons._data.is_consolidated()
    self._check_roundtrip(df[:0], tm.assert_frame_equal, path=setup_path)