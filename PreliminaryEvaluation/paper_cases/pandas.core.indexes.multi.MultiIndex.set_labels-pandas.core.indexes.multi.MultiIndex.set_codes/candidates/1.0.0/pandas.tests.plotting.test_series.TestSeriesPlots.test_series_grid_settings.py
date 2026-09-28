@pytest.mark.slow
def test_series_grid_settings(self):
    self._check_grid_settings(Series([1, 2, 3]), plotting.PlotAccessor._series_kinds + plotting.PlotAccessor._common_kinds)