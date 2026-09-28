def test_parr_add_sub_object_array(self):
    pi = pd.period_range('2000-12-31', periods=3, freq='D')
    parr = pi.array
    other = np.array([pd.Timedelta(days=1), pd.offsets.Day(2), 3])
    with tm.assert_produces_warning(PerformanceWarning):
        result = parr + other
    expected = pd.PeriodIndex(['2001-01-01', '2001-01-03', '2001-01-05'], freq='D').array
    tm.assert_equal(result, expected)
    with tm.assert_produces_warning(PerformanceWarning):
        result = parr - other
    expected = pd.PeriodIndex(['2000-12-30'] * 3, freq='D').array
    tm.assert_equal(result, expected)