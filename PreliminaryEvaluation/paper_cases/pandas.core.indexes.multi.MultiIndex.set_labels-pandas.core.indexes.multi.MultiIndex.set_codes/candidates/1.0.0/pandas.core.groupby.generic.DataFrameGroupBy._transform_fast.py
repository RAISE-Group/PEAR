def _transform_fast(self, result: DataFrame, func_nm: str) -> DataFrame:
    """
        Fast transform path for aggregations
        """
    cast = self._transform_should_cast(func_nm)
    obj = self._obj_with_exclusions
    ids, _, ngroup = self.grouper.group_info
    output = []
    for i, _ in enumerate(result.columns):
        res = algorithms.take_1d(result.iloc[:, i].values, ids)
        if cast:
            res = self._try_cast(res, obj.iloc[:, i])
        output.append(res)
    return DataFrame._from_arrays(output, columns=result.columns, index=obj.index)