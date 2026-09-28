def column_types(self):
    """Returns a numpy character array of the column types:
           s (string) or d (double)"""
    return np.asarray(self._column_types, dtype=np.dtype('S1'))