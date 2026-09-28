def _prepare_data(self):
    data = self.data
    typlist = self.typlist
    convert_dates = self._convert_dates
    if self._convert_dates is not None:
        for i, col in enumerate(data):
            if i in convert_dates:
                data[col] = _datetime_to_stata_elapsed_vec(data[col], self.fmtlist[i])
    data = self._convert_strls(data)
    dtypes = {}
    native_byteorder = self._byteorder == _set_endianness(sys.byteorder)
    for i, col in enumerate(data):
        typ = typlist[i]
        if typ <= self._max_string_length:
            data[col] = data[col].fillna('').apply(_pad_bytes, args=(typ,))
            stype = f'S{typ}'
            dtypes[col] = stype
            data[col] = data[col].astype(stype)
        else:
            dtype = data[col].dtype
            if not native_byteorder:
                dtype = dtype.newbyteorder(self._byteorder)
            dtypes[col] = dtype
    self.data = data.to_records(index=False, column_dtypes=dtypes)