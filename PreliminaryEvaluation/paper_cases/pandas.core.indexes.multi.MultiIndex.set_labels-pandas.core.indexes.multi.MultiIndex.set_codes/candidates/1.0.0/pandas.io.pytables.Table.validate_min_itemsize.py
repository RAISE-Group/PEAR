def validate_min_itemsize(self, min_itemsize):
    """validate the min_itemsize doesn't contain items that are not in the
        axes this needs data_columns to be defined
        """
    if min_itemsize is None:
        return
    if not isinstance(min_itemsize, dict):
        return
    q = self.queryables()
    for k, v in min_itemsize.items():
        if k == 'values':
            continue
        if k not in q:
            raise ValueError(f'min_itemsize has the key [{k}] which is not an axis or data_column')