def column_data_lengths(self):
    """Return a numpy int64 array of the column data lengths"""
    return np.asarray(self._column_data_lengths, dtype=np.int64)