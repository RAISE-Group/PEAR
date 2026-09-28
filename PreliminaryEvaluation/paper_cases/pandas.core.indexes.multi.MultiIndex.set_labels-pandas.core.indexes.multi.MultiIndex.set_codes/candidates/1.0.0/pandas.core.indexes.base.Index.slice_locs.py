def slice_locs(self, start=None, end=None, step=None, kind=None):
    """
        Compute slice locations for input labels.

        Parameters
        ----------
        start : label, default None
            If None, defaults to the beginning.
        end : label, default None
            If None, defaults to the end.
        step : int, defaults None
            If None, defaults to 1.
        kind : {'ix', 'loc', 'getitem'} or None

        Returns
        -------
        start, end : int

        See Also
        --------
        Index.get_loc : Get location for a single label.

        Notes
        -----
        This method only works if the index is monotonic or unique.

        Examples
        --------
        >>> idx = pd.Index(list('abcd'))
        >>> idx.slice_locs(start='b', end='c')
        (1, 3)
        """
    inc = step is None or step >= 0
    if not inc:
        start, end = (end, start)
    if isinstance(start, (str, datetime)) and isinstance(end, (str, datetime)):
        try:
            ts_start = Timestamp(start)
            ts_end = Timestamp(end)
        except (ValueError, TypeError):
            pass
        else:
            if not tz_compare(ts_start.tzinfo, ts_end.tzinfo):
                raise ValueError('Both dates must have the same UTC offset')
    start_slice = None
    if start is not None:
        start_slice = self.get_slice_bound(start, 'left', kind)
    if start_slice is None:
        start_slice = 0
    end_slice = None
    if end is not None:
        end_slice = self.get_slice_bound(end, 'right', kind)
    if end_slice is None:
        end_slice = len(self)
    if not inc:
        end_slice, start_slice = (start_slice - 1, end_slice - 1)
        if end_slice == -1:
            end_slice -= len(self)
        if start_slice == -1:
            start_slice -= len(self)
    return (start_slice, end_slice)