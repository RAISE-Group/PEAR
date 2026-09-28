def _check_ew(self, name=None, preserve_nan=False):
    series_result = getattr(self.series.ewm(com=10), name)()
    assert isinstance(series_result, Series)
    frame_result = getattr(self.frame.ewm(com=10), name)()
    assert type(frame_result) == DataFrame
    result = getattr(self.series.ewm(com=10), name)()
    if preserve_nan:
        assert result[self._nan_locs].isna().all()