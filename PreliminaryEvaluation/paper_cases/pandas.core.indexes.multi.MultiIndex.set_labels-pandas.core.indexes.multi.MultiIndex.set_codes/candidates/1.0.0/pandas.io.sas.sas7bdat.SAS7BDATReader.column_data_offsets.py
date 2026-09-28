def column_data_offsets(self):
    """Return a numpy int64 array of the column offsets"""
    return np.asarray(self._column_data_offsets, dtype=np.int64)