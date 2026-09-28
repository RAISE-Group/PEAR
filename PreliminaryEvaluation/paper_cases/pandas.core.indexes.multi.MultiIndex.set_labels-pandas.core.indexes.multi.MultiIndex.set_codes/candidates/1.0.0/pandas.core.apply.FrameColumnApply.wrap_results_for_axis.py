def wrap_results_for_axis(self, results: ResType, res_index: 'Index') -> Union['Series', 'DataFrame']:
    """ return the results for the columns """
    result: Union['Series', 'DataFrame']
    if self.result_type == 'expand':
        result = self.infer_to_same_shape(results, res_index)
    elif not isinstance(results[0], ABCSeries):
        from pandas import Series
        result = Series(results)
        result.index = res_index
    else:
        result = self.infer_to_same_shape(results, res_index)
    return result