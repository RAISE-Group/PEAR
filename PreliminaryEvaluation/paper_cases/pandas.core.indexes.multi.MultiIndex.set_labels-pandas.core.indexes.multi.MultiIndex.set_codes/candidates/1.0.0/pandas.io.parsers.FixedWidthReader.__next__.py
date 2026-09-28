def __next__(self):
    if self.buffer is not None:
        try:
            line = next(self.buffer)
        except StopIteration:
            self.buffer = None
            line = next(self.f)
    else:
        line = next(self.f)
    return [line[fromm:to].strip(self.delimiter) for fromm, to in self.colspecs]