def write_data_chunk(self, rows: np.ndarray, indexes: List[np.ndarray], mask: Optional[np.ndarray], values: List[np.ndarray]):
    """
        Parameters
        ----------
        rows : an empty memory space where we are putting the chunk
        indexes : an array of the indexes
        mask : an array of the masks
        values : an array of the values
        """
    for v in values:
        if not np.prod(v.shape):
            return
    nrows = indexes[0].shape[0]
    if nrows != len(rows):
        rows = np.empty(nrows, dtype=self.dtype)
    names = self.dtype.names
    nindexes = len(indexes)
    for i, idx in enumerate(indexes):
        rows[names[i]] = idx
    for i, v in enumerate(values):
        rows[names[i + nindexes]] = v
    if mask is not None:
        m = ~mask.ravel().astype(bool, copy=False)
        if not m.all():
            rows = rows[m]
    if len(rows):
        self.table.append(rows)
        self.table.flush()