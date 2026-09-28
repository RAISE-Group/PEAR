def test_transpose(self):
    for s in [tm.makeFloatSeries(), tm.makeStringSeries(), tm.makeObjectSeries()]:
        tm.assert_series_equal(s.transpose(), s)
    for df in [tm.makeTimeDataFrame()]:
        tm.assert_frame_equal(df.transpose().transpose(), df)