def take(self, indexer, allow_fill=False, fill_value=None):
    indexer = np.asarray(indexer)
    msg = 'Index is out of bounds or cannot do a non-empty take from an empty array.'
    if allow_fill:
        if fill_value is None:
            fill_value = self.dtype.na_value
        if (indexer < -1).any():
            raise ValueError
        try:
            output = [self.data[loc] if loc != -1 else fill_value for loc in indexer]
        except IndexError:
            raise IndexError(msg)
    else:
        try:
            output = [self.data[loc] for loc in indexer]
        except IndexError:
            raise IndexError(msg)
    return self._from_sequence(output)