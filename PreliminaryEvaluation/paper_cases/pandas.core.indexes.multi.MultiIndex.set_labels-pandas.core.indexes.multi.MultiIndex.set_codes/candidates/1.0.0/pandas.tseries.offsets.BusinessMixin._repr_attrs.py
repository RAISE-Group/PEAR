def _repr_attrs(self):
    if self.offset:
        attrs = [f'offset={repr(self.offset)}']
    else:
        attrs = None
    out = ''
    if attrs:
        out += ': ' + ', '.join(attrs)
    return out