def _badobj_wrap(self, value, func, allow_complex=True, **kwargs):
    if value.dtype.kind == 'O':
        if allow_complex:
            value = value.astype('c16')
        else:
            value = value.astype('f8')
    return func(value, **kwargs)