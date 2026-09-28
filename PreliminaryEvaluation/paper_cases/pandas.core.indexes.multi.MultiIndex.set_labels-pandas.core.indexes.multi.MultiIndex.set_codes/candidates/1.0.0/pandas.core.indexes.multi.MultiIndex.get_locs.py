def get_locs(self, seq):
    """
        Get location for a sequence of labels.

        Parameters
        ----------
        seq : label, slice, list, mask or a sequence of such
           You should use one of the above for each level.
           If a level should not be used, set it to ``slice(None)``.

        Returns
        -------
        numpy.ndarray
            NumPy array of integers suitable for passing to iloc.

        See Also
        --------
        MultiIndex.get_loc : Get location for a label or a tuple of labels.
        MultiIndex.slice_locs : Get slice location given start label(s) and
                                end label(s).

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([list('abb'), list('def')])

        >>> mi.get_locs('b')  # doctest: +SKIP
        array([1, 2], dtype=int64)

        >>> mi.get_locs([slice(None), ['e', 'f']])  # doctest: +SKIP
        array([1, 2], dtype=int64)

        >>> mi.get_locs([[True, False, True], slice('e', 'f')])  # doctest: +SKIP
        array([2], dtype=int64)
        """
    from pandas.core.indexes.numeric import Int64Index
    true_slices = [i for i, s in enumerate(com.is_true_slices(seq)) if s]
    if true_slices and true_slices[-1] >= self.lexsort_depth:
        raise UnsortedIndexError(f'MultiIndex slicing requires the index to be lexsorted: slicing on levels {true_slices}, lexsort depth {self.lexsort_depth}')
    n = len(self)
    indexer = None

    def _convert_to_indexer(r):
        if isinstance(r, slice):
            m = np.zeros(n, dtype=bool)
            m[r] = True
            r = m.nonzero()[0]
        elif com.is_bool_indexer(r):
            if len(r) != n:
                raise ValueError('cannot index with a boolean indexer that is not the same length as the index')
            r = r.nonzero()[0]
        return Int64Index(r)

    def _update_indexer(idxr, indexer=indexer):
        if indexer is None:
            indexer = Index(np.arange(n))
        if idxr is None:
            return indexer
        return indexer & idxr
    for i, k in enumerate(seq):
        if com.is_bool_indexer(k):
            k = np.asarray(k)
            indexer = _update_indexer(_convert_to_indexer(k), indexer=indexer)
        elif is_list_like(k):
            indexers = None
            for x in k:
                try:
                    idxrs = _convert_to_indexer(self._get_level_indexer(x, level=i, indexer=indexer))
                    indexers = idxrs if indexers is None else indexers | idxrs
                except KeyError:
                    continue
            if indexers is not None:
                indexer = _update_indexer(indexers, indexer=indexer)
            else:
                return Int64Index([])._ndarray_values
        elif com.is_null_slice(k):
            indexer = _update_indexer(None, indexer=indexer)
        elif isinstance(k, slice):
            indexer = _update_indexer(_convert_to_indexer(self._get_level_indexer(k, level=i, indexer=indexer)), indexer=indexer)
        else:
            indexer = _update_indexer(_convert_to_indexer(self.get_loc_level(k, level=i, drop_level=False)[0]), indexer=indexer)
    if indexer is None:
        return Int64Index([])._ndarray_values
    return indexer._ndarray_values