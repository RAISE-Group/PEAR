@property
def asi8(self) -> np.ndarray:
    """
        Integer representation of the values.

        Returns
        -------
        ndarray
            An ndarray with int64 dtype.
        """
    return self._data.view('i8')