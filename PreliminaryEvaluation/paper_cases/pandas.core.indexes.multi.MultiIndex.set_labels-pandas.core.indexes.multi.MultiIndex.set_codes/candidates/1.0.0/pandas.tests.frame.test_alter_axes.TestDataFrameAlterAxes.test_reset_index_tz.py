def test_reset_index_tz(self, tz_aware_fixture):
    tz = tz_aware_fixture
    idx = date_range('1/1/2011', periods=5, freq='D', tz=tz, name='idx')
    df = DataFrame({'a': range(5), 'b': ['A', 'B', 'C', 'D', 'E']}, index=idx)
    expected = DataFrame({'idx': [datetime(2011, 1, 1), datetime(2011, 1, 2), datetime(2011, 1, 3), datetime(2011, 1, 4), datetime(2011, 1, 5)], 'a': range(5), 'b': ['A', 'B', 'C', 'D', 'E']}, columns=['idx', 'a', 'b'])
    expected['idx'] = expected['idx'].apply(lambda d: Timestamp(d, tz=tz))
    tm.assert_frame_equal(df.reset_index(), expected)