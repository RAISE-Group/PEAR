def test_sort_non_lexsorted(self):
    idx = MultiIndex([['A', 'B', 'C'], ['c', 'b', 'a']], [[0, 1, 2, 0, 1, 2], [0, 2, 1, 1, 0, 2]])
    df = DataFrame({'col': range(len(idx))}, index=idx, dtype='int64')
    assert df.index.is_lexsorted() is False
    assert df.index.is_monotonic is False
    sorted = df.sort_index()
    assert sorted.index.is_lexsorted() is True
    assert sorted.index.is_monotonic is True
    expected = DataFrame({'col': [1, 4, 5, 2]}, index=MultiIndex.from_tuples([('B', 'a'), ('B', 'c'), ('C', 'a'), ('C', 'b')]), dtype='int64')
    result = sorted.loc[pd.IndexSlice['B':'C', 'a':'c'], :]
    tm.assert_frame_equal(result, expected)