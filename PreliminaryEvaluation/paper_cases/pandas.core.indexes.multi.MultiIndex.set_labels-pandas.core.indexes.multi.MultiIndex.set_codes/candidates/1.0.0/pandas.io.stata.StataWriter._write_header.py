def _write_header(self, data_label=None, time_stamp=None):
    byteorder = self._byteorder
    self._file.write(struct.pack('b', 114))
    self._write(byteorder == '>' and '\x01' or '\x02')
    self._write('\x01')
    self._write('\x00')
    self._file.write(struct.pack(byteorder + 'h', self.nvar)[:2])
    self._file.write(struct.pack(byteorder + 'i', self.nobs)[:4])
    if data_label is None:
        self._file.write(self._null_terminate(_pad_bytes('', 80)))
    else:
        self._file.write(self._null_terminate(_pad_bytes(data_label[:80], 80)))
    if time_stamp is None:
        time_stamp = datetime.datetime.now()
    elif not isinstance(time_stamp, datetime.datetime):
        raise ValueError('time_stamp should be datetime type')
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_lookup = {i + 1: month for i, month in enumerate(months)}
    ts = time_stamp.strftime('%d ') + month_lookup[time_stamp.month] + time_stamp.strftime(' %Y %H:%M')
    self._file.write(self._null_terminate(ts))