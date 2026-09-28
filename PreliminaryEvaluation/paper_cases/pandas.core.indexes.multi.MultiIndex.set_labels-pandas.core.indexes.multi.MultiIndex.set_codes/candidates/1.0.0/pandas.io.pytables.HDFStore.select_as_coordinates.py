def select_as_coordinates(self, key: str, where=None, start: Optional[int]=None, stop: Optional[int]=None):
    """
        return the selection as an Index

        Parameters
        ----------
        key : str
        where : list of Term (or convertible) objects, optional
        start : integer (defaults to None), row number to start selection
        stop  : integer (defaults to None), row number to stop selection
        """
    where = _ensure_term(where, scope_level=1)
    tbl = self.get_storer(key)
    if not isinstance(tbl, Table):
        raise TypeError('can only read_coordinates with a table')
    return tbl.read_coordinates(where=where, start=start, stop=stop)