def test_cumsum(self, datetime_frame):
    datetime_frame.loc[5:10, 0] = np.nan
    datetime_frame.loc[10:15, 1] = np.nan
    datetime_frame.loc[15:, 2] = np.nan
    cumsum = datetime_frame.cumsum()
    expected = datetime_frame.apply(Series.cumsum)
    tm.assert_frame_equal(cumsum, expected)
    cumsum = datetime_frame.cumsum(axis=1)
    expected = datetime_frame.apply(Series.cumsum, axis=1)
    tm.assert_frame_equal(cumsum, expected)
    df = DataFrame({'A': np.arange(20)}, index=np.arange(20))
    df.cumsum()
    cumsum_xs = datetime_frame.cumsum(axis=1)
    assert np.shape(cumsum_xs) == np.shape(datetime_frame)