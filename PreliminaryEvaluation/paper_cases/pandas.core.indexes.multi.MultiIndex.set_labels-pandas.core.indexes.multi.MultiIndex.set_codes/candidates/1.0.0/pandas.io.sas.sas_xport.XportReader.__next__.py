def __next__(self):
    return self.read(nrows=self._chunksize or 1)