def test_frame_iloc_callable(self):
    df = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': list('aabb')}, index=list('ABCD'))
    res = df.iloc[lambda x: [1, 3]]
    tm.assert_frame_equal(res, df.iloc[[1, 3]])
    res = df.iloc[lambda x: [1, 3], :]
    tm.assert_frame_equal(res, df.iloc[[1, 3], :])
    res = df.iloc[lambda x: [1, 3], lambda x: 0]
    tm.assert_series_equal(res, df.iloc[[1, 3], 0])
    res = df.iloc[lambda x: [1, 3], lambda x: [0]]
    tm.assert_frame_equal(res, df.iloc[[1, 3], [0]])
    res = df.iloc[[1, 3], lambda x: 0]
    tm.assert_series_equal(res, df.iloc[[1, 3], 0])
    res = df.iloc[[1, 3], lambda x: [0]]
    tm.assert_frame_equal(res, df.iloc[[1, 3], [0]])
    res = df.iloc[lambda x: [1, 3], 0]
    tm.assert_series_equal(res, df.iloc[[1, 3], 0])
    res = df.iloc[lambda x: [1, 3], [0]]
    tm.assert_frame_equal(res, df.iloc[[1, 3], [0]])