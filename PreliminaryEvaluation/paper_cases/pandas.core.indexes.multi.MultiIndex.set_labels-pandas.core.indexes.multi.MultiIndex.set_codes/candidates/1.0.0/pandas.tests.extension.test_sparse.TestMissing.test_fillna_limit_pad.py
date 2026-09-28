def test_fillna_limit_pad(self, data_missing):
    with tm.assert_produces_warning(PerformanceWarning):
        super().test_fillna_limit_pad(data_missing)