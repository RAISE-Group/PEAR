def test_frame_operators(self, float_frame):
    frame = float_frame
    frame2 = pd.DataFrame(float_frame, columns=['D', 'C', 'B', 'A'])
    garbage = np.random.random(4)
    colSeries = pd.Series(garbage, index=np.array(frame.columns))
    idSum = frame + frame
    seriesSum = frame + colSeries
    for col, series in idSum.items():
        for idx, val in series.items():
            origVal = frame[col][idx] * 2
            if not np.isnan(val):
                assert val == origVal
            else:
                assert np.isnan(origVal)
    for col, series in seriesSum.items():
        for idx, val in series.items():
            origVal = frame[col][idx] + colSeries[col]
            if not np.isnan(val):
                assert val == origVal
            else:
                assert np.isnan(origVal)
    added = frame2 + frame2
    expected = frame2 * 2
    tm.assert_frame_equal(added, expected)
    df = pd.DataFrame({'a': ['a', None, 'b']})
    tm.assert_frame_equal(df + df, pd.DataFrame({'a': ['aa', np.nan, 'bb']}))
    for dtype in ('float', 'int64'):
        frames = [pd.DataFrame(dtype=dtype), pd.DataFrame(columns=['A'], dtype=dtype), pd.DataFrame(index=[0], dtype=dtype)]
        for df in frames:
            assert (df + df).equals(df)
            tm.assert_frame_equal(df + df, df)