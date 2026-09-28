def test_value_counts_unique(self):
    idx = timedelta_range('1 days 09:00:00', freq='H', periods=10)
    idx = TimedeltaIndex(np.repeat(idx.values, range(1, len(idx) + 1)))
    exp_idx = timedelta_range('1 days 18:00:00', freq='-1H', periods=10)
    expected = Series(range(10, 0, -1), index=exp_idx, dtype='int64')
    for obj in [idx, Series(idx)]:
        tm.assert_series_equal(obj.value_counts(), expected)
    expected = timedelta_range('1 days 09:00:00', freq='H', periods=10)
    tm.assert_index_equal(idx.unique(), expected)
    idx = TimedeltaIndex(['1 days 09:00:00', '1 days 09:00:00', '1 days 09:00:00', '1 days 08:00:00', '1 days 08:00:00', pd.NaT])
    exp_idx = TimedeltaIndex(['1 days 09:00:00', '1 days 08:00:00'])
    expected = Series([3, 2], index=exp_idx)
    for obj in [idx, Series(idx)]:
        tm.assert_series_equal(obj.value_counts(), expected)
    exp_idx = TimedeltaIndex(['1 days 09:00:00', '1 days 08:00:00', pd.NaT])
    expected = Series([3, 2, 1], index=exp_idx)
    for obj in [idx, Series(idx)]:
        tm.assert_series_equal(obj.value_counts(dropna=False), expected)
    tm.assert_index_equal(idx.unique(), exp_idx)