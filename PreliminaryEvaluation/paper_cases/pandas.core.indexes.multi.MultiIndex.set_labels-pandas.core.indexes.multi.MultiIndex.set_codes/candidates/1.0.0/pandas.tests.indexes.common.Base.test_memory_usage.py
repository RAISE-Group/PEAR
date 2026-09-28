def test_memory_usage(self, indices):
    indices._engine.clear_mapping()
    result = indices.memory_usage()
    if indices.empty:
        assert result == 0
        return
    indices.get_loc(indices[0])
    result2 = indices.memory_usage()
    result3 = indices.memory_usage(deep=True)
    if not isinstance(indices, (RangeIndex, IntervalIndex)):
        assert result2 > result
    if indices.inferred_type == 'object':
        assert result3 > result2