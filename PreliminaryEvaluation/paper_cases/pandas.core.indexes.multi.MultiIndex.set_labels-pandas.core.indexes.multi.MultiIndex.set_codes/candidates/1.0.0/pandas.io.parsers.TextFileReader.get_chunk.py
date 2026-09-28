def get_chunk(self, size=None):
    if size is None:
        size = self.chunksize
    if self.nrows is not None:
        if self._currow >= self.nrows:
            raise StopIteration
        size = min(size, self.nrows - self._currow)
    return self.read(nrows=size)