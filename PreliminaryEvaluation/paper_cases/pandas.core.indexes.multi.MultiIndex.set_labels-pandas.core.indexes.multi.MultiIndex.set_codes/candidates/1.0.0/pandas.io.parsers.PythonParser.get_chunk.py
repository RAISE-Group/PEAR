def get_chunk(self, size=None):
    if size is None:
        size = self.chunksize
    return self.read(rows=size)