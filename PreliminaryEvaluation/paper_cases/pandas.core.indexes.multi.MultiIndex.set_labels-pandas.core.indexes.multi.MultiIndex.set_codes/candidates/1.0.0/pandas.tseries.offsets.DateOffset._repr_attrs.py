def _repr_attrs(self):
    exclude = {'n', 'inc', 'normalize'}
    attrs = []
    for attr in sorted(self.__dict__):
        if attr.startswith('_') or attr == 'kwds':
            continue
        elif attr not in exclude:
            value = getattr(self, attr)
            attrs.append(f'{attr}={value}')
    out = ''
    if attrs:
        out += ': ' + ', '.join(attrs)
    return out