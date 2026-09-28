@property
def nbytes(self):
    return sum((x.size for chunk in self._data.chunks for x in chunk.buffers() if x is not None))