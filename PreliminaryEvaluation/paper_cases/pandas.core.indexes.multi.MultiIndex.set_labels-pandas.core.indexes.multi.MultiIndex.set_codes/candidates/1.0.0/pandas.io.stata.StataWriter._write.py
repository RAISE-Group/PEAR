def _write(self, to_write):
    """
        Helper to call encode before writing to file for Python 3 compat.
        """
    self._file.write(to_write.encode(self._encoding or self._default_encoding))