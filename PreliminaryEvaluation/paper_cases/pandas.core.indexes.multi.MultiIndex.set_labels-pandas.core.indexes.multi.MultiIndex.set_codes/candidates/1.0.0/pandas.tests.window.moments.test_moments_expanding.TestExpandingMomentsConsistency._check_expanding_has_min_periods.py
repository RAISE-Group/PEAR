def _check_expanding_has_min_periods(self, func, static_comp, has_min_periods):
    ser = Series(randn(50))
    if has_min_periods:
        result = func(ser, min_periods=30)
        assert result[:29].isna().all()
        tm.assert_almost_equal(result.iloc[-1], static_comp(ser[:50]))
        result = func(ser, min_periods=15)
        assert isna(result.iloc[13])
        assert notna(result.iloc[14])
        ser2 = Series(randn(20))
        result = func(ser2, min_periods=5)
        assert isna(result[3])
        assert notna(result[4])
        result0 = func(ser, min_periods=0)
        result1 = func(ser, min_periods=1)
        tm.assert_almost_equal(result0, result1)
    else:
        result = func(ser)
        tm.assert_almost_equal(result.iloc[-1], static_comp(ser[:50]))