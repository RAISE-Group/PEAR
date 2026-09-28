def _read_value_labels(self):
    if self._value_labels_read:
        return
    if self.format_version <= 108:
        self._value_labels_read = True
        self.value_label_dict = dict()
        return
    if self.format_version >= 117:
        self.path_or_buf.seek(self.seek_value_labels)
    else:
        offset = self.nobs * self._dtype.itemsize
        self.path_or_buf.seek(self.data_location + offset)
    self._value_labels_read = True
    self.value_label_dict = dict()
    while True:
        if self.format_version >= 117:
            if self.path_or_buf.read(5) == b'</val':
                break
        slength = self.path_or_buf.read(4)
        if not slength:
            break
        if self.format_version <= 117:
            labname = self._decode(self.path_or_buf.read(33))
        else:
            labname = self._decode(self.path_or_buf.read(129))
        self.path_or_buf.read(3)
        n = struct.unpack(self.byteorder + 'I', self.path_or_buf.read(4))[0]
        txtlen = struct.unpack(self.byteorder + 'I', self.path_or_buf.read(4))[0]
        off = np.frombuffer(self.path_or_buf.read(4 * n), dtype=self.byteorder + 'i4', count=n)
        val = np.frombuffer(self.path_or_buf.read(4 * n), dtype=self.byteorder + 'i4', count=n)
        ii = np.argsort(off)
        off = off[ii]
        val = val[ii]
        txt = self.path_or_buf.read(txtlen)
        self.value_label_dict[labname] = dict()
        for i in range(n):
            end = off[i + 1] if i < n - 1 else txtlen
            self.value_label_dict[labname][val[i]] = self._decode(txt[off[i]:end])
        if self.format_version >= 117:
            self.path_or_buf.read(6)
    self._value_labels_read = True