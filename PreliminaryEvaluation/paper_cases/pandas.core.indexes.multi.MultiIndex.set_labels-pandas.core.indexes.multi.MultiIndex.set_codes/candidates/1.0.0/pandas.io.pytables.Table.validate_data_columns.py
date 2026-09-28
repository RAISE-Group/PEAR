def validate_data_columns(self, data_columns, min_itemsize, non_index_axes):
    """take the input data_columns and min_itemize and create a data
        columns spec
        """
    if not len(non_index_axes):
        return []
    axis, axis_labels = non_index_axes[0]
    info = self.info.get(axis, dict())
    if info.get('type') == 'MultiIndex' and data_columns:
        raise ValueError(f'cannot use a multi-index on axis [{axis}] with data_columns {data_columns}')
    if data_columns is True:
        data_columns = list(axis_labels)
    elif data_columns is None:
        data_columns = []
    if isinstance(min_itemsize, dict):
        existing_data_columns = set(data_columns)
        data_columns = list(data_columns)
        data_columns.extend([k for k in min_itemsize.keys() if k != 'values' and k not in existing_data_columns])
    return [c for c in data_columns if c in axis_labels]