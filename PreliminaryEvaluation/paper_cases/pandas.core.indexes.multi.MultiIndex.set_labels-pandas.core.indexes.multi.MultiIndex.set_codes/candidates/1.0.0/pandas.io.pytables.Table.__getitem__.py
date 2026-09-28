def __getitem__(self, c: str):
    """ return the axis for c """
    for a in self.axes:
        if c == a.name:
            return a
    return None