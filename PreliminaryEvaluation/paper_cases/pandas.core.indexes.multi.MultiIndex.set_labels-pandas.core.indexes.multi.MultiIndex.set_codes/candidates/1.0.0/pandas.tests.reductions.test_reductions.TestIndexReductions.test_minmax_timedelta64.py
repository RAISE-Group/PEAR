def test_minmax_timedelta64(self):
    idx1 = TimedeltaIndex(['1 days', '2 days', '3 days'])
    assert idx1.is_monotonic
    idx2 = TimedeltaIndex(['1 days', np.nan, '3 days', 'NaT'])
    assert not idx2.is_monotonic
    for idx in [idx1, idx2]:
        assert idx.min() == Timedelta('1 days')
        assert idx.max() == Timedelta('3 days')
        assert idx.argmin() == 0
        assert idx.argmax() == 2
    for op in ['min', 'max']:
        obj = TimedeltaIndex([])
        assert pd.isna(getattr(obj, op)())
        obj = TimedeltaIndex([pd.NaT])
        assert pd.isna(getattr(obj, op)())
        obj = TimedeltaIndex([pd.NaT, pd.NaT, pd.NaT])
        assert pd.isna(getattr(obj, op)())