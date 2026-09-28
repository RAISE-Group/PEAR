def infer_to_same_shape(self, results: ResType, res_index: 'Index') -> 'DataFrame':
    """ infer the results to the same shape as the input object """
    result = self.obj._constructor(data=results)
    result = result.T
    result.index = res_index
    result = result.infer_objects()
    return result