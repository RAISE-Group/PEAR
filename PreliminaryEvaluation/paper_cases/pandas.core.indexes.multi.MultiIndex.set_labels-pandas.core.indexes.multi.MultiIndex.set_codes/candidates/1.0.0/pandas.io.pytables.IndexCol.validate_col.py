def validate_col(self, itemsize=None):
    """ validate this column: return the compared against itemsize """
    if _ensure_decoded(self.kind) == 'string':
        c = self.col
        if c is not None:
            if itemsize is None:
                itemsize = self.itemsize
            if c.itemsize < itemsize:
                raise ValueError(f'Trying to store a string with len [{itemsize}] in [{self.cname}] column but\nthis column has a limit of [{c.itemsize}]!\nConsider using min_itemsize to preset the sizes on these columns')
            return c.itemsize
    return None