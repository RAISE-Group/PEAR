def _partial_date_slice(self, reso: str, parsed, use_lhs: bool=True, use_rhs: bool=True):
    """
        Parameters
        ----------
        reso : str
        use_lhs : bool, default True
        use_rhs : bool, default True
        """
    is_monotonic = self.is_monotonic
    if is_monotonic and reso in ['day', 'hour', 'minute', 'second'] and (self._resolution >= Resolution.get_reso(reso)):
        raise KeyError
    if reso == 'microsecond':
        raise KeyError
    t1, t2 = self._parsed_string_to_bounds(reso, parsed)
    stamps = self.asi8
    if is_monotonic:
        if len(stamps) and (use_lhs and t1.value < stamps[0] and (t2.value < stamps[0]) or (use_rhs and t1.value > stamps[-1] and (t2.value > stamps[-1]))):
            raise KeyError
        left = stamps.searchsorted(t1.value, side='left') if use_lhs else None
        right = stamps.searchsorted(t2.value, side='right') if use_rhs else None
        return slice(left, right)
    lhs_mask = stamps >= t1.value if use_lhs else True
    rhs_mask = stamps <= t2.value if use_rhs else True
    return (lhs_mask & rhs_mask).nonzero()[0]