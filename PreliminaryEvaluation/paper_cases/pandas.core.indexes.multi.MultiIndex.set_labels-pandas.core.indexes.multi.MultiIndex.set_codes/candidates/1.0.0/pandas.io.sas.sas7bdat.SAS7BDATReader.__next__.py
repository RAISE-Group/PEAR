def __next__(self):
    da = self.read(nrows=self.chunksize or 1)
    if da is None:
        raise StopIteration
    return da