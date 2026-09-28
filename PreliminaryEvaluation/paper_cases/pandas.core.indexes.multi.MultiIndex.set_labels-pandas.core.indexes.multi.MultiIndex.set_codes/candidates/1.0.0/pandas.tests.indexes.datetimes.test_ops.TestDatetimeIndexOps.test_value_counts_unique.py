def test_value_counts_unique(self, tz_naive_fixture):
    tz = tz_naive_fixture
    idx = pd.date_range('2011-01-01 09:00', freq='H', periods=10)
    idx = DatetimeIndex(np.repeat(idx.values, range(1, len(idx) + 1)), tz=tz)
    exp_idx = pd.date_range('2011-01-01 18:00', freq='-1H', periods=10, tz=tz)
    expected = Series(range(10, 0, -1), index=exp_idx, dtype='int64')
    for obj in [idx, Series(idx)]:
        tm.assert_series_equal(obj.value_counts(), expected)
    expected = pd.date_range('2011-01-01 09:00', freq='H', periods=10, tz=tz)
    tm.assert_index_equal(idx.unique(), expected)
    idx = DatetimeIndex(['2013-01-01 09:00', '2013-01-01 09:00', '2013-01-01 09:00', '2013-01-01 08:00', '2013-01-01 08:00', pd.NaT], tz=tz)
    exp_idx = DatetimeIndex(['2013-01-01 09:00', '2013-01-01 08:00'], tz=tz)
    expected = Series([3, 2], index=exp_idx)
    for obj in [idx, Series(idx)]:
        tm.assert_series_equal(obj.value_counts(), expected)
    exp_idx = DatetimeIndex(['2013-01-01 09:00', '2013-01-01 08:00', pd.NaT], tz=tz)
    expected = Series([3, 2, 1], index=exp_idx)
    for obj in [idx, Series(idx)]:
        tm.assert_series_equal(obj.value_counts(dropna=False), expected)
    tm.assert_index_equal(idx.unique(), exp_idx)