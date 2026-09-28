def duplicated(self, subset: Optional[Union[Hashable, Sequence[Hashable]]]=None, keep: Union[str, bool]='first') -> 'Series':
    """
        Return boolean Series denoting duplicate rows.

        Considering certain columns is optional.

        Parameters
        ----------
        subset : column label or sequence of labels, optional
            Only consider certain columns for identifying duplicates, by
            default use all of the columns.
        keep : {'first', 'last', False}, default 'first'
            Determines which duplicates (if any) to mark.

            - ``first`` : Mark duplicates as ``True`` except for the first occurrence.
            - ``last`` : Mark duplicates as ``True`` except for the last occurrence.
            - False : Mark all duplicates as ``True``.

        Returns
        -------
        Series
        """
    from pandas.core.sorting import get_group_index
    from pandas._libs.hashtable import duplicated_int64, _SIZE_HINT_LIMIT
    if self.empty:
        return Series(dtype=bool)

    def f(vals):
        labels, shape = algorithms.factorize(vals, size_hint=min(len(self), _SIZE_HINT_LIMIT))
        return (labels.astype('i8', copy=False), len(shape))
    if subset is None:
        subset = self.columns
    elif not np.iterable(subset) or isinstance(subset, str) or (isinstance(subset, tuple) and subset in self.columns):
        subset = (subset,)
    subset = cast(Iterable, subset)
    diff = Index(subset).difference(self.columns)
    if not diff.empty:
        raise KeyError(diff)
    vals = (col.values for name, col in self.items() if name in subset)
    labels, shape = map(list, zip(*map(f, vals)))
    ids = get_group_index(labels, shape, sort=False, xnull=False)
    return Series(duplicated_int64(ids, keep), index=self.index)