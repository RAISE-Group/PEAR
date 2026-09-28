def test_timedelta64_operations_with_DateOffset(self):
    td = Series([timedelta(minutes=5, seconds=3)] * 3)
    result = td + pd.offsets.Minute(1)
    expected = Series([timedelta(minutes=6, seconds=3)] * 3)
    tm.assert_series_equal(result, expected)
    result = td - pd.offsets.Minute(1)
    expected = Series([timedelta(minutes=4, seconds=3)] * 3)
    tm.assert_series_equal(result, expected)
    with tm.assert_produces_warning(PerformanceWarning):
        result = td + Series([pd.offsets.Minute(1), pd.offsets.Second(3), pd.offsets.Hour(2)])
    expected = Series([timedelta(minutes=6, seconds=3), timedelta(minutes=5, seconds=6), timedelta(hours=2, minutes=5, seconds=3)])
    tm.assert_series_equal(result, expected)
    result = td + pd.offsets.Minute(1) + pd.offsets.Second(12)
    expected = Series([timedelta(minutes=6, seconds=15)] * 3)
    tm.assert_series_equal(result, expected)
    for do in ['Hour', 'Minute', 'Second', 'Day', 'Micro', 'Milli', 'Nano']:
        op = getattr(pd.offsets, do)
        td + op(5)
        op(5) + td
        td - op(5)
        op(5) - td