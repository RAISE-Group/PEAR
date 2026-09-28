def test_searchsorted(self, data_for_sorting, as_series):
    with tm.assert_produces_warning(PerformanceWarning):
        super().test_searchsorted(data_for_sorting, as_series)