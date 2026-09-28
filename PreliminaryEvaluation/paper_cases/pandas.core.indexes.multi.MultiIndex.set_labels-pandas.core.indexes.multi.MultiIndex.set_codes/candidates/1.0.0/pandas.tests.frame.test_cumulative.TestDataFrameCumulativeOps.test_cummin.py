def test_cummin(self, datetime_frame):
    datetime_frame.loc[5:10, 0] = np.nan
    datetime_frame.loc[10:15, 1] = np.nan
    datetime_frame.loc[15:, 2] = np.nan
    cummin = datetime_frame.cummin()
    expected = datetime_frame.apply(Series.cummin)
    tm.assert_frame_equal(cummin, expected)
    cummin = datetime_frame.cummin(axis=1)
    expected = datetime_frame.apply(Series.cummin, axis=1)
    tm.assert_frame_equal(cummin, expected)
    df = DataFrame({'A': np.arange(20)}, index=np.arange(20))
    df.cummin()
    cummin_xs = datetime_frame.cummin(axis=1)
    assert np.shape(cummin_xs) == np.shape(datetime_frame)