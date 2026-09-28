def _sanitize_column(self, key, value, broadcast=True):
    """
        Ensures new columns (which go into the BlockManager as new blocks) are
        always copied and converted into an array.

        Parameters
        ----------
        key : object
        value : scalar, Series, or array-like
        broadcast : bool, default True
            If ``key`` matches multiple duplicate column names in the
            DataFrame, this parameter indicates whether ``value`` should be
            tiled so that the returned array contains a (duplicated) column for
            each occurrence of the key. If False, ``value`` will not be tiled.

        Returns
        -------
        numpy.ndarray
        """

    def reindexer(value):
        if value.index.equals(self.index) or not len(self.index):
            value = value._values.copy()
        else:
            try:
                value = value.reindex(self.index)._values
            except ValueError as err:
                if not value.index.is_unique:
                    raise err
                raise TypeError('incompatible index of inserted column with frame index')
        return value
    if isinstance(value, Series):
        value = reindexer(value)
    elif isinstance(value, DataFrame):
        if isinstance(self.columns, ABCMultiIndex) and key in self.columns:
            loc = self.columns.get_loc(key)
            if isinstance(loc, (slice, Series, np.ndarray, Index)):
                cols = maybe_droplevels(self.columns[loc], key)
                if len(cols) and (not cols.equals(value.columns)):
                    value = value.reindex(cols, axis=1)
        value = reindexer(value).T
    elif isinstance(value, ExtensionArray):
        value = value.copy()
        value = sanitize_index(value, self.index, copy=False)
    elif isinstance(value, Index) or is_sequence(value):
        value = sanitize_index(value, self.index, copy=False)
        if not isinstance(value, (np.ndarray, Index)):
            if isinstance(value, list) and len(value) > 0:
                value = maybe_convert_platform(value)
            else:
                value = com.asarray_tuplesafe(value)
        elif value.ndim == 2:
            value = value.copy().T
        elif isinstance(value, Index):
            value = value.copy(deep=True)
        else:
            value = value.copy()
        if is_object_dtype(value.dtype):
            value = maybe_infer_to_datetimelike(value)
    else:
        infer_dtype, _ = infer_dtype_from_scalar(value, pandas_dtype=True)
        value = cast_scalar_to_array(len(self.index), value)
        value = maybe_cast_to_datetime(value, infer_dtype)
    if is_extension_array_dtype(value):
        return value
    if broadcast and key in self.columns and (value.ndim == 1):
        if not self.columns.is_unique or isinstance(self.columns, ABCMultiIndex):
            existing_piece = self[key]
            if isinstance(existing_piece, DataFrame):
                value = np.tile(value, (len(existing_piece.columns), 1))
    return np.atleast_2d(np.asarray(value))