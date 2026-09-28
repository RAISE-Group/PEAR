@classmethod
def get_atom_data(cls, shape, kind: str) -> 'Col':
    return cls.get_atom_coltype(kind=kind)(shape=shape[0])