def get_result(self, coordinates: bool=False):
    if self.chunksize is not None:
        if not isinstance(self.s, Table):
            raise TypeError('can only use an iterator or chunksize on a table')
        self.coordinates = self.s.read_coordinates(where=self.where)
        return self
    if coordinates:
        if not isinstance(self.s, Table):
            raise TypeError('can only read_coordinates on a table')
        where = self.s.read_coordinates(where=self.where, start=self.start, stop=self.stop)
    else:
        where = self.where
    results = self.func(self.start, self.stop, where)
    self.close()
    return results