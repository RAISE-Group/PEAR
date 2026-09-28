def view(self, dtype=None) -> Union[ABCExtensionArray, np.ndarray]:
    """
        Return a view on the array.

        Parameters
        ----------
        dtype : str, np.dtype, or ExtensionDtype, optional
            Default None.

        Returns
        -------
        ExtensionArray
            A view of the :class:`ExtensionArray`.
        """
    if dtype is not None:
        raise NotImplementedError(dtype)
    return self[:]