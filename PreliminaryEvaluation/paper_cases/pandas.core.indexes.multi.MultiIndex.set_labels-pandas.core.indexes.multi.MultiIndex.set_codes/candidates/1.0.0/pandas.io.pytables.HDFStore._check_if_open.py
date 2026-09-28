def _check_if_open(self):
    if not self.is_open:
        raise ClosedFileError(f'{self._path} file is not open!')