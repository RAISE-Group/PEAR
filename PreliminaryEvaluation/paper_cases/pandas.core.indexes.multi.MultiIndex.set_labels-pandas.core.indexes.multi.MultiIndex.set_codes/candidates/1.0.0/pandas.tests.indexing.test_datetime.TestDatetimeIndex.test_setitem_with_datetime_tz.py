def test_setitem_with_datetime_tz(self):
    mask = np.array([True, False, True, False])
    idx = date_range('20010101', periods=4, tz='UTC')
    df = DataFrame({'a': np.arange(4)}, index=idx).astype('float64')
    result = df.copy()
    result.loc[mask, :] = df.loc[mask, :]
    tm.assert_frame_equal(result, df)
    result = df.copy()
    result.loc[mask] = df.loc[mask]
    tm.assert_frame_equal(result, df)
    idx = date_range('20010101', periods=4)
    df = DataFrame({'a': np.arange(4)}, index=idx).astype('float64')
    result = df.copy()
    result.loc[mask, :] = df.loc[mask, :]
    tm.assert_frame_equal(result, df)
    result = df.copy()
    result.loc[mask] = df.loc[mask]
    tm.assert_frame_equal(result, df)