def __repr__(self) -> str:
    """ return a pretty representation of myself """
    self.infer_axes()
    s = self.shape
    if s is not None:
        if isinstance(s, (list, tuple)):
            jshape = ','.join((pprint_thing(x) for x in s))
            s = f'[{jshape}]'
        return f'{self.pandas_type:12.12} (shape->{s})'
    return self.pandas_type