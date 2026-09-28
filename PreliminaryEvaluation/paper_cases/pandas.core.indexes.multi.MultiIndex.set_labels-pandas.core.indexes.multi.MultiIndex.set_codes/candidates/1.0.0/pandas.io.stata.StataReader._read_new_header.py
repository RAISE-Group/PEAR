def _read_new_header(self, first_char):
    self.path_or_buf.read(27)
    self.format_version = int(self.path_or_buf.read(3))
    if self.format_version not in [117, 118, 119]:
        raise ValueError(_version_error.format(version=self.format_version))
    self._set_encoding()
    self.path_or_buf.read(21)
    self.byteorder = self.path_or_buf.read(3) == b'MSF' and '>' or '<'
    self.path_or_buf.read(15)
    nvar_type = 'H' if self.format_version <= 118 else 'I'
    nvar_size = 2 if self.format_version <= 118 else 4
    self.nvar = struct.unpack(self.byteorder + nvar_type, self.path_or_buf.read(nvar_size))[0]
    self.path_or_buf.read(7)
    self.nobs = self._get_nobs()
    self.path_or_buf.read(11)
    self._data_label = self._get_data_label()
    self.path_or_buf.read(19)
    self.time_stamp = self._get_time_stamp()
    self.path_or_buf.read(26)
    self.path_or_buf.read(8)
    self.path_or_buf.read(8)
    self._seek_vartypes = struct.unpack(self.byteorder + 'q', self.path_or_buf.read(8))[0] + 16
    self._seek_varnames = struct.unpack(self.byteorder + 'q', self.path_or_buf.read(8))[0] + 10
    self._seek_sortlist = struct.unpack(self.byteorder + 'q', self.path_or_buf.read(8))[0] + 10
    self._seek_formats = struct.unpack(self.byteorder + 'q', self.path_or_buf.read(8))[0] + 9
    self._seek_value_label_names = struct.unpack(self.byteorder + 'q', self.path_or_buf.read(8))[0] + 19
    self._seek_variable_labels = self._get_seek_variable_labels()
    self.path_or_buf.read(8)
    self.data_location = struct.unpack(self.byteorder + 'q', self.path_or_buf.read(8))[0] + 6
    self.seek_strls = struct.unpack(self.byteorder + 'q', self.path_or_buf.read(8))[0] + 7
    self.seek_value_labels = struct.unpack(self.byteorder + 'q', self.path_or_buf.read(8))[0] + 14
    self.typlist, self.dtyplist = self._get_dtypes(self._seek_vartypes)
    self.path_or_buf.seek(self._seek_varnames)
    self.varlist = self._get_varlist()
    self.path_or_buf.seek(self._seek_sortlist)
    self.srtlist = struct.unpack(self.byteorder + 'h' * (self.nvar + 1), self.path_or_buf.read(2 * (self.nvar + 1)))[:-1]
    self.path_or_buf.seek(self._seek_formats)
    self.fmtlist = self._get_fmtlist()
    self.path_or_buf.seek(self._seek_value_label_names)
    self.lbllist = self._get_lbllist()
    self.path_or_buf.seek(self._seek_variable_labels)
    self._variable_labels = self._get_variable_labels()