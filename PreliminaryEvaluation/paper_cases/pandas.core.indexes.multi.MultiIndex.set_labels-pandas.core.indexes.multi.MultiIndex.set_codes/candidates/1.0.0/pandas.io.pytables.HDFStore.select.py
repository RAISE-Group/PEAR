def select(self, key: str, where=None, start=None, stop=None, columns=None, iterator=False, chunksize=None, auto_close: bool=False):
    """
        Retrieve pandas object stored in file, optionally based on where criteria.

        Parameters
        ----------
        key : str
                Object being retrieved from file.
        where : list, default None
                List of Term (or convertible) objects, optional.
        start : int, default None
                Row number to start selection.
        stop : int, default None
                Row number to stop selection.
        columns : list, default None
                A list of columns that if not None, will limit the return columns.
        iterator : bool, default False
                Returns an iterator.
        chunksize : int, default None
                Number or rows to include in iteration, return an iterator.
        auto_close : bool, default False
            Should automatically close the store when finished.

        Returns
        -------
        object
            Retrieved object from file.
        """
    group = self.get_node(key)
    if group is None:
        raise KeyError(f'No object named {key} in the file')
    where = _ensure_term(where, scope_level=1)
    s = self._create_storer(group)
    s.infer_axes()

    def func(_start, _stop, _where):
        return s.read(start=_start, stop=_stop, where=_where, columns=columns)
    it = TableIterator(self, s, func, where=where, nrows=s.nrows, start=start, stop=stop, iterator=iterator, chunksize=chunksize, auto_close=auto_close)
    return it.get_result()