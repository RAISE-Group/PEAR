def _check_moment_func(self, static_comp, name, raw, has_min_periods=True, has_center=True, has_time_rule=True, fill_value=None, zero_min_periods_equal=True, **kwargs):
    if name == 'apply':
        kwargs = copy.copy(kwargs)
        kwargs['raw'] = raw

    def get_result(obj, window, min_periods=None, center=False):
        r = obj.rolling(window=window, min_periods=min_periods, center=center)
        return getattr(r, name)(**kwargs)
    series_result = get_result(self.series, window=50)
    assert isinstance(series_result, Series)
    tm.assert_almost_equal(series_result.iloc[-1], static_comp(self.series[-50:]))
    frame_result = get_result(self.frame, window=50)
    assert isinstance(frame_result, DataFrame)
    tm.assert_series_equal(frame_result.iloc[-1, :], self.frame.iloc[-50:, :].apply(static_comp, axis=0, raw=raw), check_names=False)
    if has_time_rule:
        win = 25
        minp = 10
        series = self.series[::2].resample('B').mean()
        frame = self.frame[::2].resample('B').mean()
        if has_min_periods:
            series_result = get_result(series, window=win, min_periods=minp)
            frame_result = get_result(frame, window=win, min_periods=minp)
        else:
            series_result = get_result(series, window=win, min_periods=0)
            frame_result = get_result(frame, window=win, min_periods=0)
        last_date = series_result.index[-1]
        prev_date = last_date - 24 * offsets.BDay()
        trunc_series = self.series[::2].truncate(prev_date, last_date)
        trunc_frame = self.frame[::2].truncate(prev_date, last_date)
        tm.assert_almost_equal(series_result[-1], static_comp(trunc_series))
        tm.assert_series_equal(frame_result.xs(last_date), trunc_frame.apply(static_comp, raw=raw), check_names=False)
    obj = Series(randn(50))
    obj[:10] = np.NaN
    obj[-10:] = np.NaN
    if has_min_periods:
        result = get_result(obj, 50, min_periods=30)
        tm.assert_almost_equal(result.iloc[-1], static_comp(obj[10:-10]))
        result = get_result(obj, 20, min_periods=15)
        assert isna(result.iloc[23])
        assert not isna(result.iloc[24])
        assert not isna(result.iloc[-6])
        assert isna(result.iloc[-5])
        obj2 = Series(randn(20))
        result = get_result(obj2, 10, min_periods=5)
        assert isna(result.iloc[3])
        assert notna(result.iloc[4])
        if zero_min_periods_equal:
            result0 = get_result(obj, 20, min_periods=0)
            result1 = get_result(obj, 20, min_periods=1)
            tm.assert_almost_equal(result0, result1)
    else:
        result = get_result(obj, 50)
        tm.assert_almost_equal(result.iloc[-1], static_comp(obj[10:-10]))
    if has_min_periods:
        for minp in (0, len(self.series) - 1, len(self.series)):
            result = get_result(self.series, len(self.series) + 1, min_periods=minp)
            expected = get_result(self.series, len(self.series), min_periods=minp)
            nan_mask = isna(result)
            tm.assert_series_equal(nan_mask, isna(expected))
            nan_mask = ~nan_mask
            tm.assert_almost_equal(result[nan_mask], expected[nan_mask])
    else:
        result = get_result(self.series, len(self.series) + 1, min_periods=0)
        expected = get_result(self.series, len(self.series), min_periods=0)
        nan_mask = isna(result)
        tm.assert_series_equal(nan_mask, isna(expected))
        nan_mask = ~nan_mask
        tm.assert_almost_equal(result[nan_mask], expected[nan_mask])
    if has_center:
        if has_min_periods:
            result = get_result(obj, 20, min_periods=15, center=True)
            expected = get_result(pd.concat([obj, Series([np.NaN] * 9)]), 20, min_periods=15)[9:].reset_index(drop=True)
        else:
            result = get_result(obj, 20, min_periods=0, center=True)
            print(result)
            expected = get_result(pd.concat([obj, Series([np.NaN] * 9)]), 20, min_periods=0)[9:].reset_index(drop=True)
        tm.assert_series_equal(result, expected)
        s = ['x{x:d}'.format(x=x) for x in range(12)]
        if has_min_periods:
            minp = 10
            series_xp = get_result(self.series.reindex(list(self.series.index) + s), window=25, min_periods=minp).shift(-12).reindex(self.series.index)
            frame_xp = get_result(self.frame.reindex(list(self.frame.index) + s), window=25, min_periods=minp).shift(-12).reindex(self.frame.index)
            series_rs = get_result(self.series, window=25, min_periods=minp, center=True)
            frame_rs = get_result(self.frame, window=25, min_periods=minp, center=True)
        else:
            series_xp = get_result(self.series.reindex(list(self.series.index) + s), window=25, min_periods=0).shift(-12).reindex(self.series.index)
            frame_xp = get_result(self.frame.reindex(list(self.frame.index) + s), window=25, min_periods=0).shift(-12).reindex(self.frame.index)
            series_rs = get_result(self.series, window=25, min_periods=0, center=True)
            frame_rs = get_result(self.frame, window=25, min_periods=0, center=True)
        if fill_value is not None:
            series_xp = series_xp.fillna(fill_value)
            frame_xp = frame_xp.fillna(fill_value)
        tm.assert_series_equal(series_xp, series_rs)
        tm.assert_frame_equal(frame_xp, frame_rs)