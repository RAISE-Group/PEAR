def test_append_hierarchical(self, setup_path):
    index = MultiIndex(levels=[['foo', 'bar', 'baz', 'qux'], ['one', 'two', 'three']], codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]], names=['foo', 'bar'])
    df = DataFrame(np.random.randn(10, 3), index=index, columns=['A', 'B', 'C'])
    with ensure_clean_store(setup_path) as store:
        store.append('mi', df)
        result = store.select('mi')
        tm.assert_frame_equal(result, df)
        result = store.select('mi', columns=['A', 'B'])
        expected = df.reindex(columns=['A', 'B'])
        tm.assert_frame_equal(result, expected)
    with ensure_clean_path('test.hdf') as path:
        df.to_hdf(path, 'df', format='table')
        result = read_hdf(path, 'df', columns=['A', 'B'])
        expected = df.reindex(columns=['A', 'B'])
        tm.assert_frame_equal(result, expected)