def __repr__(self) -> str:
    temp = tuple(map(pprint_thing, (self.name, self.cname, self.axis, self.pos, self.kind)))
    return ','.join((f'{key}->{value}' for key, value in zip(['name', 'cname', 'axis', 'pos', 'kind'], temp)))