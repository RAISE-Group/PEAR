def test_value_counts_unique(self):
    idx = pd.period_range('2011-01-01 09:00', freq='H', periods=10)
    idx = PeriodIndex(np.repeat(idx._values, range(1, len(idx) + 1)), freq='H')
    exp_idx = PeriodIndex(['2011-01-01 18:00', '2011-01-01 17:00', '2011-01-01 16:00', '2011-01-01 15:00', '2011-01-01 14:00', '2011-01-01 13:00', '2011-01-01 12:00', '2011-01-01 11:00', '2011-01-01 10:00', '2011-01-01 09:00'], freq='H')
    expected = Series(range(10, 0, -1), index=exp_idx, dtype='int64')
    for obj in [idx, Series(idx)]:
        tm.assert_series_equal(obj.value_counts(), expected)
    expected = pd.period_range('2011-01-01 09:00', freq='H', periods=10)
    tm.assert_index_equal(idx.unique(), expected)
    idx = PeriodIndex(['2013-01-01 09:00', '2013-01-01 09:00', '2013-01-01 09:00', '2013-01-01 08:00', '2013-01-01 08:00', NaT], freq='H')
    exp_idx = PeriodIndex(['2013-01-01 09:00', '2013-01-01 08:00'], freq='H')
    expected = Series([3, 2], index=exp_idx)
    for obj in [idx, Series(idx)]:
        tm.assert_series_equal(obj.value_counts(), expected)
    exp_idx = PeriodIndex(['2013-01-01 09:00', '2013-01-01 08:00', NaT], freq='H')
    expected = Series([3, 2, 1], index=exp_idx)
    for obj in [idx, Series(idx)]:
        tm.assert_series_equal(obj.value_counts(dropna=False), expected)
    tm.assert_index_equal(idx.unique(), exp_idx)