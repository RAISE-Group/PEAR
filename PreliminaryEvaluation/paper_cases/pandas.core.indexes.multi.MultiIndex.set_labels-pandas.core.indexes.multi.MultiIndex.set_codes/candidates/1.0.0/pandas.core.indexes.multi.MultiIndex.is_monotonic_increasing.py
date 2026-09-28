@cache_readonly
def is_monotonic_increasing(self) -> bool:
    """
        return if the index is monotonic increasing (only equal or
        increasing) values.
        """
    if all((x.is_monotonic for x in self.levels)):
        return libalgos.is_lexsorted([x.astype('int64', copy=False) for x in self.codes])
    values = [self._get_level_values(i).values for i in reversed(range(len(self.levels)))]
    try:
        sort_order = np.lexsort(values)
        return Index(sort_order).is_monotonic
    except TypeError:
        return Index(self.values).is_monotonic