def test_cummax(self, datetime_frame):
    datetime_frame.loc[5:10, 0] = np.nan
    datetime_frame.loc[10:15, 1] = np.nan
    datetime_frame.loc[15:, 2] = np.nan
    cummax = datetime_frame.cummax()
    expected = datetime_frame.apply(Series.cummax)
    tm.assert_frame_equal(cummax, expected)
    cummax = datetime_frame.cummax(axis=1)
    expected = datetime_frame.apply(Series.cummax, axis=1)
    tm.assert_frame_equal(cummax, expected)
    df = DataFrame({'A': np.arange(20)}, index=np.arange(20))
    df.cummax()
    cummax_xs = datetime_frame.cummax(axis=1)
    assert np.shape(cummax_xs) == np.shape(datetime_frame)