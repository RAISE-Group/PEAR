def _close(self):
    """
        Close the file if it was created by the writer.

        If a buffer or file-like object was passed in, for example a GzipFile,
        then leave this file open for the caller to close. In either case,
        attempt to flush the file contents to ensure they are written to disk
        (if supported)
        """
    try:
        self._file.flush()
    except AttributeError:
        pass
    if self._own_file:
        self._file.close()