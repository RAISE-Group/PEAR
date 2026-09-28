def _write_file_close_tag(self):
    self._update_map('stata_data_close')
    self._file.write(bytes('</stata_dta>', 'utf-8'))
    self._update_map('end-of-file')