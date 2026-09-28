def insert_data(self):
    if self.index is not None:
        temp = self.frame.copy()
        temp.index.names = self.index
        try:
            temp.reset_index(inplace=True)
        except ValueError as err:
            raise ValueError(f'duplicate name in index/columns: {err}')
    else:
        temp = self.frame
    column_names = list(map(str, temp.columns))
    ncols = len(column_names)
    data_list = [None] * ncols
    blocks = temp._data.blocks
    for b in blocks:
        if b.is_datetime:
            if b.is_datetimetz:
                d = b.values.to_pydatetime()
                d = np.atleast_2d(d)
            else:
                d = b.values.astype('M8[us]').astype(object)
        else:
            d = np.array(b.get_values(), dtype=object)
        if b._can_hold_na:
            mask = isna(d)
            d[mask] = None
        for col_loc, col in zip(b.mgr_locs, d):
            data_list[col_loc] = col
    return (column_names, data_list)