def wrap_results(self, results: ResType, res_index: 'Index') -> Union['Series', 'DataFrame']:
    from pandas import Series
    if len(results) > 0 and 0 in results and is_sequence(results[0]):
        return self.wrap_results_for_axis(results, res_index)
    constructor_sliced = self.obj._constructor_sliced
    if constructor_sliced is Series:
        result = create_series_with_explicit_dtype(results, dtype_if_empty=np.float64)
    else:
        result = constructor_sliced(results)
    result.index = res_index
    return result