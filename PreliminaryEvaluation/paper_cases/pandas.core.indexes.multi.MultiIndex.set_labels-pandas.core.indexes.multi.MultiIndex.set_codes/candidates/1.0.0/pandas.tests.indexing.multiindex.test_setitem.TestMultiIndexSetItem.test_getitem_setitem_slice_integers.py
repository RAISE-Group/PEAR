def test_getitem_setitem_slice_integers(self):
    index = MultiIndex(levels=[[0, 1, 2], [0, 2]], codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])
    frame = DataFrame(np.random.randn(len(index), 4), index=index, columns=['a', 'b', 'c', 'd'])
    res = frame.loc[1:2]
    exp = frame.reindex(frame.index[2:])
    tm.assert_frame_equal(res, exp)
    frame.loc[1:2] = 7
    assert (frame.loc[1:2] == 7).values.all()
    series = Series(np.random.randn(len(index)), index=index)
    res = series.loc[1:2]
    exp = series.reindex(series.index[2:])
    tm.assert_series_equal(res, exp)
    series.loc[1:2] = 7
    assert (series.loc[1:2] == 7).values.all()