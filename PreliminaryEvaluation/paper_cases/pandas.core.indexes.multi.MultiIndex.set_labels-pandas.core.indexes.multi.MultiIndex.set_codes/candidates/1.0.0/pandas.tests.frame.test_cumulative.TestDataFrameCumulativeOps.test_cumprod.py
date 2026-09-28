def test_cumprod(self, datetime_frame):
    datetime_frame.loc[5:10, 0] = np.nan
    datetime_frame.loc[10:15, 1] = np.nan
    datetime_frame.loc[15:, 2] = np.nan
    cumprod = datetime_frame.cumprod()
    expected = datetime_frame.apply(Series.cumprod)
    tm.assert_frame_equal(cumprod, expected)
    cumprod = datetime_frame.cumprod(axis=1)
    expected = datetime_frame.apply(Series.cumprod, axis=1)
    tm.assert_frame_equal(cumprod, expected)
    cumprod_xs = datetime_frame.cumprod(axis=1)
    assert np.shape(cumprod_xs) == np.shape(datetime_frame)
    df = datetime_frame.fillna(0).astype(int)
    df.cumprod(0)
    df.cumprod(1)
    df = datetime_frame.fillna(0).astype(np.int32)
    df.cumprod(0)
    df.cumprod(1)