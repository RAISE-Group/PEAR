def test_groupby_empty(self):
    s = pd.Series([], name='name', dtype='float64')
    gr = s.groupby([])
    result = gr.mean()
    tm.assert_series_equal(result, s)
    assert len(gr.grouper.groupings) == 1
    tm.assert_numpy_array_equal(gr.grouper.group_info[0], np.array([], dtype=np.dtype('int64')))
    tm.assert_numpy_array_equal(gr.grouper.group_info[1], np.array([], dtype=np.dtype('int')))
    assert gr.grouper.group_info[2] == 0
    assert s.groupby(s).grouper.names == ['name']