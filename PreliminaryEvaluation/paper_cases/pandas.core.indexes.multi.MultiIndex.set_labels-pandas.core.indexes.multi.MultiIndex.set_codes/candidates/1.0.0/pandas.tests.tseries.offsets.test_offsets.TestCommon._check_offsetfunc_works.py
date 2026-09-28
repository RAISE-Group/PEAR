def _check_offsetfunc_works(self, offset, funcname, dt, expected, normalize=False):
    if normalize and issubclass(offset, Tick):
        return
    offset_s = self._get_offset(offset, normalize=normalize)
    func = getattr(offset_s, funcname)
    result = func(dt)
    assert isinstance(result, Timestamp)
    assert result == expected
    result = func(Timestamp(dt))
    assert isinstance(result, Timestamp)
    assert result == expected
    exp_warning = None
    ts = Timestamp(dt) + Nano(5)
    if type(offset_s).__name__ == 'DateOffset' and (funcname == 'apply' or normalize) and (ts.nanosecond > 0):
        exp_warning = UserWarning
    with tm.assert_produces_warning(exp_warning, check_stacklevel=False):
        result = func(ts)
    assert isinstance(result, Timestamp)
    if normalize is False:
        assert result == expected + Nano(5)
    else:
        assert result == expected
    if isinstance(dt, np.datetime64):
        return
    for tz in self.timezones:
        expected_localize = expected.tz_localize(tz)
        tz_obj = timezones.maybe_get_tz(tz)
        dt_tz = conversion.localize_pydatetime(dt, tz_obj)
        result = func(dt_tz)
        assert isinstance(result, Timestamp)
        assert result == expected_localize
        result = func(Timestamp(dt, tz=tz))
        assert isinstance(result, Timestamp)
        assert result == expected_localize
        exp_warning = None
        ts = Timestamp(dt, tz=tz) + Nano(5)
        if type(offset_s).__name__ == 'DateOffset' and (funcname == 'apply' or normalize) and (ts.nanosecond > 0):
            exp_warning = UserWarning
        with tm.assert_produces_warning(exp_warning, check_stacklevel=False):
            result = func(ts)
        assert isinstance(result, Timestamp)
        if normalize is False:
            assert result == expected_localize + Nano(5)
        else:
            assert result == expected_localize