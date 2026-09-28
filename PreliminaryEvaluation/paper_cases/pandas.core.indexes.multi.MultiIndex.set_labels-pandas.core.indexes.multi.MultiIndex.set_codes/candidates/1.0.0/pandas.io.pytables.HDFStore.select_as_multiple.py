def select_as_multiple(self, keys, where=None, selector=None, columns=None, start=None, stop=None, iterator=False, chunksize=None, auto_close: bool=False):
    """
        Retrieve pandas objects from multiple tables.

        Parameters
        ----------
        keys : a list of the tables
        selector : the table to apply the where criteria (defaults to keys[0]
            if not supplied)
        columns : the columns I want back
        start : integer (defaults to None), row number to start selection
        stop  : integer (defaults to None), row number to stop selection
        iterator : boolean, return an iterator, default False
        chunksize : nrows to include in iteration, return an iterator
        auto_close : bool, default False
            Should automatically close the store when finished.

        Raises
        ------
        raises KeyError if keys or selector is not found or keys is empty
        raises TypeError if keys is not a list or tuple
        raises ValueError if the tables are not ALL THE SAME DIMENSIONS
        """
    where = _ensure_term(where, scope_level=1)
    if isinstance(keys, (list, tuple)) and len(keys) == 1:
        keys = keys[0]
    if isinstance(keys, str):
        return self.select(key=keys, where=where, columns=columns, start=start, stop=stop, iterator=iterator, chunksize=chunksize, auto_close=auto_close)
    if not isinstance(keys, (list, tuple)):
        raise TypeError('keys must be a list/tuple')
    if not len(keys):
        raise ValueError('keys must have a non-zero length')
    if selector is None:
        selector = keys[0]
    tbls = [self.get_storer(k) for k in keys]
    s = self.get_storer(selector)
    nrows = None
    for t, k in itertools.chain([(s, selector)], zip(tbls, keys)):
        if t is None:
            raise KeyError(f'Invalid table [{k}]')
        if not t.is_table:
            raise TypeError(f'object [{t.pathname}] is not a table, and cannot be used in all select as multiple')
        if nrows is None:
            nrows = t.nrows
        elif t.nrows != nrows:
            raise ValueError('all tables must have exactly the same nrows!')
    _tbls = [x for x in tbls if isinstance(x, Table)]
    axis = list({t.non_index_axes[0][0] for t in _tbls})[0]

    def func(_start, _stop, _where):
        objs = [t.read(where=_where, columns=columns, start=_start, stop=_stop) for t in tbls]
        return concat(objs, axis=axis, verify_integrity=False)._consolidate()
    it = TableIterator(self, s, func, where=where, nrows=nrows, start=start, stop=stop, iterator=iterator, chunksize=chunksize, auto_close=auto_close)
    return it.get_result(coordinates=True)