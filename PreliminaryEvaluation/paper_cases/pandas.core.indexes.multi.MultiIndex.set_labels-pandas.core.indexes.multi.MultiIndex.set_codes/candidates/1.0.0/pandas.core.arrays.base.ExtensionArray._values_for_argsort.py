def _values_for_argsort(self) -> np.ndarray:
    """
        Return values for sorting.

        Returns
        -------
        ndarray
            The transformed values should maintain the ordering between values
            within the array.

        See Also
        --------
        ExtensionArray.argsort
        """
    return np.array(self)