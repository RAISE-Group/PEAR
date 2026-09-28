def _read_old_header(self, first_char):
    self.format_version = struct.unpack('b', first_char)[0]
    if self.format_version not in [104, 105, 108, 111, 113, 114, 115]:
        raise ValueError(_version_error.format(version=self.format_version))
    self._set_encoding()
    self.byteorder = struct.unpack('b', self.path_or_buf.read(1))[0] == 1 and '>' or '<'
    self.filetype = struct.unpack('b', self.path_or_buf.read(1))[0]
    self.path_or_buf.read(1)
    self.nvar = struct.unpack(self.byteorder + 'H', self.path_or_buf.read(2))[0]
    self.nobs = self._get_nobs()
    self._data_label = self._get_data_label()
    self.time_stamp = self._get_time_stamp()
    if self.format_version > 108:
        typlist = [ord(self.path_or_buf.read(1)) for i in range(self.nvar)]
    else:
        buf = self.path_or_buf.read(self.nvar)
        typlistb = np.frombuffer(buf, dtype=np.uint8)
        typlist = []
        for tp in typlistb:
            if tp in self.OLD_TYPE_MAPPING:
                typlist.append(self.OLD_TYPE_MAPPING[tp])
            else:
                typlist.append(tp - 127)
    try:
        self.typlist = [self.TYPE_MAP[typ] for typ in typlist]
    except ValueError:
        invalid_types = ','.join((str(x) for x in typlist))
        raise ValueError(f'cannot convert stata types [{invalid_types}]')
    try:
        self.dtyplist = [self.DTYPE_MAP[typ] for typ in typlist]
    except ValueError:
        invalid_dtypes = ','.join((str(x) for x in typlist))
        raise ValueError(f'cannot convert stata dtypes [{invalid_dtypes}]')
    if self.format_version > 108:
        self.varlist = [self._decode(self.path_or_buf.read(33)) for i in range(self.nvar)]
    else:
        self.varlist = [self._decode(self.path_or_buf.read(9)) for i in range(self.nvar)]
    self.srtlist = struct.unpack(self.byteorder + 'h' * (self.nvar + 1), self.path_or_buf.read(2 * (self.nvar + 1)))[:-1]
    self.fmtlist = self._get_fmtlist()
    self.lbllist = self._get_lbllist()
    self._variable_labels = self._get_variable_labels()
    if self.format_version > 104:
        while True:
            data_type = struct.unpack(self.byteorder + 'b', self.path_or_buf.read(1))[0]
            if self.format_version > 108:
                data_len = struct.unpack(self.byteorder + 'i', self.path_or_buf.read(4))[0]
            else:
                data_len = struct.unpack(self.byteorder + 'h', self.path_or_buf.read(2))[0]
            if data_type == 0:
                break
            self.path_or_buf.read(data_len)
    self.data_location = self.path_or_buf.tell()