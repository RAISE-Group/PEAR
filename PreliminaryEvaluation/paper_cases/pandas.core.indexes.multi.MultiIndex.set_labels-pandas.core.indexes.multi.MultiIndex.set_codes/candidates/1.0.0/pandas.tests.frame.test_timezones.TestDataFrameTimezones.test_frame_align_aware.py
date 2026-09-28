def test_frame_align_aware(self):
    idx1 = date_range('2001', periods=5, freq='H', tz='US/Eastern')
    idx2 = date_range('2001', periods=5, freq='2H', tz='US/Eastern')
    df1 = DataFrame(np.random.randn(len(idx1), 3), idx1)
    df2 = DataFrame(np.random.randn(len(idx2), 3), idx2)
    new1, new2 = df1.align(df2)
    assert df1.index.tz == new1.index.tz
    assert df2.index.tz == new2.index.tz
    df1_central = df1.tz_convert('US/Central')
    new1, new2 = df1.align(df1_central)
    assert new1.index.tz == pytz.UTC
    assert new2.index.tz == pytz.UTC
    new1, new2 = df1.align(df1_central[0], axis=0)
    assert new1.index.tz == pytz.UTC
    assert new2.index.tz == pytz.UTC
    df1[0].align(df1_central, axis=0)
    assert new1.index.tz == pytz.UTC
    assert new2.index.tz == pytz.UTC