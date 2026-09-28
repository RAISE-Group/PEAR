def factorize(self, na_sentinel: int=-1) -> Tuple[np.ndarray, ABCExtensionArray]:
    """
        Encode the extension array as an enumerated type.

        Parameters
        ----------
        na_sentinel : int, default -1
            Value to use in the `codes` array to indicate missing values.

        Returns
        -------
        codes : ndarray
            An integer NumPy array that's an indexer into the original
            ExtensionArray.
        uniques : ExtensionArray
            An ExtensionArray containing the unique values of `self`.

            .. note::

               uniques will *not* contain an entry for the NA value of
               the ExtensionArray if there are any missing values present
               in `self`.

        See Also
        --------
        factorize : Top-level factorize method that dispatches here.

        Notes
        -----
        :meth:`pandas.factorize` offers a `sort` keyword as well.
        """
    arr, na_value = self._values_for_factorize()
    codes, uniques = _factorize_array(arr, na_sentinel=na_sentinel, na_value=na_value)
    uniques = self._from_factorized(uniques, self)
    return (codes, uniques)