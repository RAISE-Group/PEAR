def test_frame_values_with_tz(self):
    tz = 'US/Central'
    df = DataFrame({'A': date_range('2000', periods=4, tz=tz)})
    result = df.values
    expected = np.array([[pd.Timestamp('2000-01-01', tz=tz)], [pd.Timestamp('2000-01-02', tz=tz)], [pd.Timestamp('2000-01-03', tz=tz)], [pd.Timestamp('2000-01-04', tz=tz)]])
    tm.assert_numpy_array_equal(result, expected)
    df = df.assign(B=df.A)
    result = df.values
    expected = np.concatenate([expected, expected], axis=1)
    tm.assert_numpy_array_equal(result, expected)
    est = 'US/Eastern'
    df = df.assign(C=df.A.dt.tz_convert(est))
    new = np.array([[pd.Timestamp('2000-01-01T01:00:00', tz=est)], [pd.Timestamp('2000-01-02T01:00:00', tz=est)], [pd.Timestamp('2000-01-03T01:00:00', tz=est)], [pd.Timestamp('2000-01-04T01:00:00', tz=est)]])
    expected = np.concatenate([expected, new], axis=1)
    result = df.values
    tm.assert_numpy_array_equal(result, expected)