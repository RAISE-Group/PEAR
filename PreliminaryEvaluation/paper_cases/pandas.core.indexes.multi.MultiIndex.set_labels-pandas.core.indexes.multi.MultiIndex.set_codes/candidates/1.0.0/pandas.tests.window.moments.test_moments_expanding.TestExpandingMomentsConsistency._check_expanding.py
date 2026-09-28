def _check_expanding(self, func, static_comp, preserve_nan=True):
    series_result = func(self.series)
    assert isinstance(series_result, Series)
    frame_result = func(self.frame)
    assert isinstance(frame_result, DataFrame)
    result = func(self.series)
    tm.assert_almost_equal(result[10], static_comp(self.series[:11]))
    if preserve_nan:
        assert result.iloc[self._nan_locs].isna().all()