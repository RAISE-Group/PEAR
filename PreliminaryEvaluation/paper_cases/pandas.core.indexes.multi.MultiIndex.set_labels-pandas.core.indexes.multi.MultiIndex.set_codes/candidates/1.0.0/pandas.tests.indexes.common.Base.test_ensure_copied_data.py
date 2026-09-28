def test_ensure_copied_data(self, indices):
    init_kwargs = {}
    if isinstance(indices, PeriodIndex):
        init_kwargs['freq'] = indices.freq
    elif isinstance(indices, (RangeIndex, MultiIndex, CategoricalIndex)):
        return
    index_type = type(indices)
    result = index_type(indices.values, copy=True, **init_kwargs)
    tm.assert_index_equal(indices, result)
    tm.assert_numpy_array_equal(indices._ndarray_values, result._ndarray_values, check_same='copy')
    if isinstance(indices, PeriodIndex):
        result = index_type(ordinal=indices.asi8, copy=False, **init_kwargs)
        tm.assert_numpy_array_equal(indices._ndarray_values, result._ndarray_values, check_same='same')
    elif isinstance(indices, IntervalIndex):
        pass
    else:
        result = index_type(indices.values, copy=False, **init_kwargs)
        tm.assert_numpy_array_equal(indices.values, result.values, check_same='same')
        tm.assert_numpy_array_equal(indices._ndarray_values, result._ndarray_values, check_same='same')