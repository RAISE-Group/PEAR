def __repr__(self) -> str:
    temp = tuple(map(pprint_thing, (self.name, self.cname, self.dtype, self.kind, self.shape)))
    return ','.join((f'{key}->{value}' for key, value in zip(['name', 'cname', 'dtype', 'kind', 'shape'], temp)))