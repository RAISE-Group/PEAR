def _write_strls(self):
    self._update_map('strls')
    strls = b''
    if self._strl_blob is not None:
        strls = self._strl_blob
    self._file.write(self._tag(strls, 'strls'))