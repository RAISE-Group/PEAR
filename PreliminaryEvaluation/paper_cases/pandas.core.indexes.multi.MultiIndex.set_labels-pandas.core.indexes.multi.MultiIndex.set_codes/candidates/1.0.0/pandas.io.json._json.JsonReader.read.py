def read(self):
    """
        Read the whole JSON input into a pandas object.
        """
    if self.lines and self.chunksize:
        obj = concat(self)
    elif self.lines:
        data = ensure_str(self.data)
        obj = self._get_object_parser(self._combine_lines(data.split('\n')))
    else:
        obj = self._get_object_parser(self.data)
    self.close()
    return obj