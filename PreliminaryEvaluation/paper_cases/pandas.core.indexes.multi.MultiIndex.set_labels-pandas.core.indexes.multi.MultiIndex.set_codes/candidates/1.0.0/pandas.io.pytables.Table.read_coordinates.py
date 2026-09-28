def read_coordinates(self, where=None, start: Optional[int]=None, stop: Optional[int]=None):
    """select coordinates (row numbers) from a table; return the
        coordinates object
        """
    self.validate_version(where)
    if not self.infer_axes():
        return False
    selection = Selection(self, where=where, start=start, stop=stop)
    coords = selection.select_coords()
    if selection.filter is not None:
        for field, op, filt in selection.filter.format():
            data = self.read_column(field, start=coords.min(), stop=coords.max() + 1)
            coords = coords[op(data.iloc[coords - coords.min()], filt).values]
    return Index(coords)