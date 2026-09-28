def test_store_hierarchical(self, setup_path):
    index = MultiIndex(levels=[['foo', 'bar', 'baz', 'qux'], ['one', 'two', 'three']], codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]], names=['foo', 'bar'])
    frame = DataFrame(np.random.randn(10, 3), index=index, columns=['A', 'B', 'C'])
    self._check_roundtrip(frame, tm.assert_frame_equal, path=setup_path)
    self._check_roundtrip(frame.T, tm.assert_frame_equal, path=setup_path)
    self._check_roundtrip(frame['A'], tm.assert_series_equal, path=setup_path)
    with ensure_clean_store(setup_path) as store:
        store['frame'] = frame
        recons = store['frame']
        tm.assert_frame_equal(recons, frame)