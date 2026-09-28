def close(self):
    """
        If we opened a stream earlier, in _get_data_from_filepath, we should
        close it.

        If an open stream or file was passed, we leave it open.
        """
    if self.should_close:
        try:
            self.open_stream.close()
        except (IOError, AttributeError):
            pass