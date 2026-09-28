def _write_header(self, data_label=None, time_stamp=None):
    """Write the file header"""
    byteorder = self._byteorder
    self._file.write(bytes('<stata_dta>', 'utf-8'))
    bio = BytesIO()
    bio.write(self._tag(bytes(str(self._dta_version), 'utf-8'), 'release'))
    bio.write(self._tag(byteorder == '>' and 'MSF' or 'LSF', 'byteorder'))
    nvar_type = 'H' if self._dta_version <= 118 else 'I'
    bio.write(self._tag(struct.pack(byteorder + nvar_type, self.nvar), 'K'))
    nobs_size = 'I' if self._dta_version == 117 else 'Q'
    bio.write(self._tag(struct.pack(byteorder + nobs_size, self.nobs), 'N'))
    label = data_label[:80] if data_label is not None else ''
    label = label.encode(self._encoding)
    label_size = 'B' if self._dta_version == 117 else 'H'
    label_len = struct.pack(byteorder + label_size, len(label))
    label = label_len + label
    bio.write(self._tag(label, 'label'))
    if time_stamp is None:
        time_stamp = datetime.datetime.now()
    elif not isinstance(time_stamp, datetime.datetime):
        raise ValueError('time_stamp should be datetime type')
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_lookup = {i + 1: month for i, month in enumerate(months)}
    ts = time_stamp.strftime('%d ') + month_lookup[time_stamp.month] + time_stamp.strftime(' %Y %H:%M')
    ts = b'\x11' + bytes(ts, 'utf-8')
    bio.write(self._tag(ts, 'timestamp'))
    bio.seek(0)
    self._file.write(self._tag(bio.read(), 'header'))