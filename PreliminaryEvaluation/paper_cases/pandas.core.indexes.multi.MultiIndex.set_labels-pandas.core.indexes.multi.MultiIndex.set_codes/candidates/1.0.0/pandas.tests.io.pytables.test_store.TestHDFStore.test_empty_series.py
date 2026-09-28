@td.xfail_non_writeable
@pytest.mark.parametrize('dtype', [np.int64, np.float64, np.object, 'm8[ns]', 'M8[ns]'])
def test_empty_series(self, dtype, setup_path):
    s = Series(dtype=dtype)
    self._check_roundtrip(s, tm.assert_series_equal, path=setup_path)