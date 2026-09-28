def test_unicode_index(self, setup_path):
    unicode_values = ['σ', 'σσ']
    with catch_warnings(record=True):
        simplefilter('ignore', pd.errors.PerformanceWarning)
        s = Series(np.random.randn(len(unicode_values)), unicode_values)
        self._check_roundtrip(s, tm.assert_series_equal, path=setup_path)