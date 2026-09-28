def write_file(self):
    self._file, self._own_file = _open_file_binary_write(self._fname)
    try:
        self._write_header(data_label=self._data_label, time_stamp=self._time_stamp)
        self._write_map()
        self._write_variable_types()
        self._write_varnames()
        self._write_sortlist()
        self._write_formats()
        self._write_value_label_names()
        self._write_variable_labels()
        self._write_expansion_fields()
        self._write_characteristics()
        self._prepare_data()
        self._write_data()
        self._write_strls()
        self._write_value_labels()
        self._write_file_close_tag()
        self._write_map()
    except Exception as exc:
        self._close()
        if self._own_file:
            try:
                os.unlink(self._fname)
            except OSError:
                warnings.warn(f'This save was not successful but {self._fname} could not be deleted.  This file is not valid.', ResourceWarning)
        raise exc
    else:
        self._close()