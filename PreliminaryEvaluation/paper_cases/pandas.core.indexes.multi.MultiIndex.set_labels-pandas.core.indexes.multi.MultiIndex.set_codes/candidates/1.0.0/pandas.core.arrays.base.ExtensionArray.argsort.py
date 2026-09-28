def argsort(self, ascending: bool=True, kind: str='quicksort', *args, **kwargs) -> np.ndarray:
    """
        Return the indices that would sort this array.

        Parameters
        ----------
        ascending : bool, default True
            Whether the indices should result in an ascending
            or descending sort.
        kind : {'quicksort', 'mergesort', 'heapsort'}, optional
            Sorting algorithm.
        *args, **kwargs:
            passed through to :func:`numpy.argsort`.

        Returns
        -------
        ndarray
            Array of indices that sort ``self``. If NaN values are contained,
            NaN values are placed at the end.

        See Also
        --------
        numpy.argsort : Sorting implementation used internally.
        """
    ascending = nv.validate_argsort_with_ascending(ascending, args, kwargs)
    result = nargsort(self, kind=kind, ascending=ascending, na_position='last')
    return result