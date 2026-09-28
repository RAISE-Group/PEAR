def test_concat_multiindex_with_keys(self):
    index = MultiIndex(levels=[['foo', 'bar', 'baz', 'qux'], ['one', 'two', 'three']], codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]], names=['first', 'second'])
    frame = DataFrame(np.random.randn(10, 3), index=index, columns=Index(['A', 'B', 'C'], name='exp'))
    result = concat([frame, frame], keys=[0, 1], names=['iteration'])
    assert result.index.names == ('iteration',) + index.names
    tm.assert_frame_equal(result.loc[0], frame)
    tm.assert_frame_equal(result.loc[1], frame)
    assert result.index.nlevels == 3