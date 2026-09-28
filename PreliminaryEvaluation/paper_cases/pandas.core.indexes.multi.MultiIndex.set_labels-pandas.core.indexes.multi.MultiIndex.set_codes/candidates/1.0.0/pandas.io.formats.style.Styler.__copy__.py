def __copy__(self):
    """
        Deep copy by default.
        """
    return self._copy(deepcopy=False)