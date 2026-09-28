def test_take(self):
    indices = [1, 5, -2, 6, 3, -1]
    for s in [tm.makeFloatSeries(), tm.makeStringSeries(), tm.makeObjectSeries()]:
        out = s.take(indices)
        expected = Series(data=s.values.take(indices), index=s.index.take(indices), dtype=s.dtype)
        tm.assert_series_equal(out, expected)
    for df in [tm.makeTimeDataFrame()]:
        out = df.take(indices)
        expected = DataFrame(data=df.values.take(indices, axis=0), index=df.index.take(indices), columns=df.columns)
        tm.assert_frame_equal(out, expected)