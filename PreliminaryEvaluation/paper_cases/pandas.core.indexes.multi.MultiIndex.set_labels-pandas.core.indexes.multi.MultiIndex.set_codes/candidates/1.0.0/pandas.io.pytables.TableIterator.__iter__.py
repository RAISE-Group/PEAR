def __iter__(self):
    current = self.start
    while current < self.stop:
        stop = min(current + self.chunksize, self.stop)
        value = self.func(None, None, self.coordinates[current:stop])
        current = stop
        if value is None or not len(value):
            continue
        yield value
    self.close()