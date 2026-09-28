@pytest.mark.parametrize('min_periods', [0, 1])
@pytest.mark.parametrize('name', ['mean', 'var', 'vol'])
def test_ew_min_periods(self, min_periods, name):
    arr = randn(50)
    arr[:10] = np.NaN
    arr[-10:] = np.NaN
    s = Series(arr)
    result = getattr(s.ewm(com=50, min_periods=2), name)()
    assert result[:11].isna().all()
    assert not result[11:].isna().any()
    result = getattr(s.ewm(com=50, min_periods=min_periods), name)()
    if name == 'mean':
        assert result[:10].isna().all()
        assert not result[10:].isna().any()
    else:
        assert result[:11].isna().all()
        assert not result[11:].isna().any()
    result = getattr(Series(dtype=object).ewm(com=50, min_periods=min_periods), name)()
    tm.assert_series_equal(result, Series(dtype='float64'))
    result = getattr(Series([1.0]).ewm(50, min_periods=min_periods), name)()
    if name == 'mean':
        tm.assert_series_equal(result, Series([1.0]))
    else:
        tm.assert_series_equal(result, Series([np.NaN]))
    result2 = getattr(Series(np.arange(50)).ewm(span=10), name)()
    assert result2.dtype == np.float_