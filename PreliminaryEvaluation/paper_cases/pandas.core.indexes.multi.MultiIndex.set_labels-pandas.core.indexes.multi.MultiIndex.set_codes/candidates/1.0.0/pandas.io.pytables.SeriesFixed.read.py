def read(self, where=None, columns=None, start: Optional[int]=None, stop: Optional[int]=None):
    self.validate_read(columns, where)
    index = self.read_index('index', start=start, stop=stop)
    values = self.read_array('values', start=start, stop=stop)
    return Series(values, index=index, name=self.name)