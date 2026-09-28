def select_column(self, key: str, column: str, start: Optional[int]=None, stop: Optional[int]=None):
    """
        return a single column from the table. This is generally only useful to
        select an indexable

        Parameters
        ----------
        key : str
        column : str
            The column of interest.
        start : int or None, default None
        stop : int or None, default None

        Raises
        ------
        raises KeyError if the column is not found (or key is not a valid
            store)
        raises ValueError if the column can not be extracted individually (it
            is part of a data block)

        """
    tbl = self.get_storer(key)
    if not isinstance(tbl, Table):
        raise TypeError('can only read_column with a table')
    return tbl.read_column(column=column, start=start, stop=stop)