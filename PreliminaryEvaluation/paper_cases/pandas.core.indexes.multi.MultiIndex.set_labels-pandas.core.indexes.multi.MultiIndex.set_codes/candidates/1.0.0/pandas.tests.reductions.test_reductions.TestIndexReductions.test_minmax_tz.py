def test_minmax_tz(self, tz_naive_fixture):
    tz = tz_naive_fixture
    idx1 = pd.DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], tz=tz)
    assert idx1.is_monotonic
    idx2 = pd.DatetimeIndex(['2011-01-01', pd.NaT, '2011-01-03', '2011-01-02', pd.NaT], tz=tz)
    assert not idx2.is_monotonic
    for idx in [idx1, idx2]:
        assert idx.min() == Timestamp('2011-01-01', tz=tz)
        assert idx.max() == Timestamp('2011-01-03', tz=tz)
        assert idx.argmin() == 0
        assert idx.argmax() == 2