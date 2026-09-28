@Appender(_read_method_doc)
def read(self, nrows=None, convert_dates=None, convert_categoricals=None, index_col=None, convert_missing=None, preserve_dtypes=None, columns=None, order_categoricals=None):
    if self.nobs == 0 and nrows is None:
        self._can_read_value_labels = True
        self._data_read = True
        self.close()
        return DataFrame(columns=self.varlist)
    if convert_dates is None:
        convert_dates = self._convert_dates
    if convert_categoricals is None:
        convert_categoricals = self._convert_categoricals
    if convert_missing is None:
        convert_missing = self._convert_missing
    if preserve_dtypes is None:
        preserve_dtypes = self._preserve_dtypes
    if columns is None:
        columns = self._columns
    if order_categoricals is None:
        order_categoricals = self._order_categoricals
    if index_col is None:
        index_col = self._index_col
    if nrows is None:
        nrows = self.nobs
    if self.format_version >= 117 and (not self._value_labels_read):
        self._can_read_value_labels = True
        self._read_strls()
    dtype = self._dtype
    max_read_len = (self.nobs - self._lines_read) * dtype.itemsize
    read_len = nrows * dtype.itemsize
    read_len = min(read_len, max_read_len)
    if read_len <= 0:
        if convert_categoricals:
            self._read_value_labels()
        self.close()
        raise StopIteration
    offset = self._lines_read * dtype.itemsize
    self.path_or_buf.seek(self.data_location + offset)
    read_lines = min(nrows, self.nobs - self._lines_read)
    data = np.frombuffer(self.path_or_buf.read(read_len), dtype=dtype, count=read_lines)
    self._lines_read += read_lines
    if self._lines_read == self.nobs:
        self._can_read_value_labels = True
        self._data_read = True
    if self.byteorder != self._native_byteorder:
        data = data.byteswap().newbyteorder()
    if convert_categoricals:
        self._read_value_labels()
    if len(data) == 0:
        data = DataFrame(columns=self.varlist)
    else:
        data = DataFrame.from_records(data)
        data.columns = self.varlist
    if index_col is None:
        ix = np.arange(self._lines_read - read_lines, self._lines_read)
        data = data.set_index(ix)
    if columns is not None:
        try:
            data = self._do_select_columns(data, columns)
        except ValueError:
            self.close()
            raise
    for col, typ in zip(data, self.typlist):
        if type(typ) is int:
            data[col] = data[col].apply(self._decode, convert_dtype=True)
    data = self._insert_strls(data)
    cols_ = np.where(self.dtyplist)[0]
    ix = data.index
    requires_type_conversion = False
    data_formatted = []
    for i in cols_:
        if self.dtyplist[i] is not None:
            col = data.columns[i]
            dtype = data[col].dtype
            if dtype != np.dtype(object) and dtype != self.dtyplist[i]:
                requires_type_conversion = True
                data_formatted.append((col, Series(data[col], ix, self.dtyplist[i])))
            else:
                data_formatted.append((col, data[col]))
    if requires_type_conversion:
        data = DataFrame.from_dict(dict(data_formatted))
    del data_formatted
    data = self._do_convert_missing(data, convert_missing)
    if convert_dates:

        def any_startswith(x: str) -> bool:
            return any((x.startswith(fmt) for fmt in _date_formats))
        cols = np.where([any_startswith(x) for x in self.fmtlist])[0]
        for i in cols:
            col = data.columns[i]
            try:
                data[col] = _stata_elapsed_date_to_datetime_vec(data[col], self.fmtlist[i])
            except ValueError:
                self.close()
                raise
    if convert_categoricals and self.format_version > 108:
        data = self._do_convert_categoricals(data, self.value_label_dict, self.lbllist, order_categoricals)
    if not preserve_dtypes:
        retyped_data = []
        convert = False
        for col in data:
            dtype = data[col].dtype
            if dtype in (np.float16, np.float32):
                dtype = np.float64
                convert = True
            elif dtype in (np.int8, np.int16, np.int32):
                dtype = np.int64
                convert = True
            retyped_data.append((col, data[col].astype(dtype)))
        if convert:
            data = DataFrame.from_dict(dict(retyped_data))
    if index_col is not None:
        data = data.set_index(data.pop(index_col))
    return data