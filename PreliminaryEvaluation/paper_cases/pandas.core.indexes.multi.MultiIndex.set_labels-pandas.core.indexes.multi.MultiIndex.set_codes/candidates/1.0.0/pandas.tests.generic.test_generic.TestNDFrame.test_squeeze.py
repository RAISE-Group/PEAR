def test_squeeze(self):
    for s in [tm.makeFloatSeries(), tm.makeStringSeries(), tm.makeObjectSeries()]:
        tm.assert_series_equal(s.squeeze(), s)
    for df in [tm.makeTimeDataFrame()]:
        tm.assert_frame_equal(df.squeeze(), df)
    df = tm.makeTimeDataFrame().reindex(columns=['A'])
    tm.assert_series_equal(df.squeeze(), df['A'])
    empty_series = Series([], name='five', dtype=np.float64)
    empty_frame = DataFrame([empty_series])
    tm.assert_series_equal(empty_series, empty_series.squeeze())
    tm.assert_series_equal(empty_series, empty_frame.squeeze())
    df = tm.makeTimeDataFrame(nper=1).iloc[:, :1]
    assert df.shape == (1, 1)
    tm.assert_series_equal(df.squeeze(axis=0), df.iloc[0])
    tm.assert_series_equal(df.squeeze(axis='index'), df.iloc[0])
    tm.assert_series_equal(df.squeeze(axis=1), df.iloc[:, 0])
    tm.assert_series_equal(df.squeeze(axis='columns'), df.iloc[:, 0])
    assert df.squeeze() == df.iloc[0, 0]
    msg = "No axis named 2 for object type <class 'pandas.core.frame.DataFrame'>"
    with pytest.raises(ValueError, match=msg):
        df.squeeze(axis=2)
    msg = "No axis named x for object type <class 'pandas.core.frame.DataFrame'>"
    with pytest.raises(ValueError, match=msg):
        df.squeeze(axis='x')
    df = tm.makeTimeDataFrame(3)
    tm.assert_frame_equal(df.squeeze(axis=0), df)