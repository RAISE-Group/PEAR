def _transform_item_by_item(self, obj: DataFrame, wrapper) -> DataFrame:
    output = {}
    inds = []
    for i, col in enumerate(obj):
        try:
            output[col] = self[col].transform(wrapper)
        except TypeError:
            pass
        else:
            inds.append(i)
    if len(output) == 0:
        raise TypeError('Transform function invalid for data types')
    columns = obj.columns
    if len(output) < len(obj.columns):
        columns = columns.take(inds)
    return DataFrame(output, index=obj.index, columns=columns)