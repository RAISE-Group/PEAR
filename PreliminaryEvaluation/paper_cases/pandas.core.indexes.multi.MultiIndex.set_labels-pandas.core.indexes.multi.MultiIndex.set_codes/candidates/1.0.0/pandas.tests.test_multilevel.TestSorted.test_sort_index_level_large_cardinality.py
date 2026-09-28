def test_sort_index_level_large_cardinality(self):
    index = MultiIndex.from_arrays([np.arange(4000)] * 3)
    df = DataFrame(np.random.randn(4000), index=index, dtype=np.int64)
    result = df.sort_index(level=0)
    assert result.index.lexsort_depth == 3
    index = MultiIndex.from_arrays([np.arange(4000)] * 3)
    df = DataFrame(np.random.randn(4000), index=index, dtype=np.int32)
    result = df.sort_index(level=0)
    assert (result.dtypes.values == df.dtypes.values).all()
    assert result.index.lexsort_depth == 3