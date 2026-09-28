def create_table_index(self, key: str, columns=None, optlevel: Optional[int]=None, kind: Optional[str]=None):
    """
        Create a pytables index on the table.

        Parameters
        ----------
        key : str
        columns : None, bool, or listlike[str]
            Indicate which columns to create an index on.

            * False : Do not create any indexes.
            * True : Create indexes on all columns.
            * None : Create indexes on all columns.
            * listlike : Create indexes on the given columns.

        optlevel : int or None, default None
            Optimization level, if None, pytables defaults to 6.
        kind : str or None, default None
            Kind of index, if None, pytables defaults to "medium".

        Raises
        ------
        TypeError: raises if the node is not a table
        """
    _tables()
    s = self.get_storer(key)
    if s is None:
        return
    if not isinstance(s, Table):
        raise TypeError('cannot create table index on a Fixed format store')
    s.create_index(columns=columns, optlevel=optlevel, kind=kind)