@classmethod
def get_atom_coltype(cls, kind: str) -> Type['Col']:
    """ return the PyTables column class for this column """
    if kind.startswith('uint'):
        k4 = kind[4:]
        col_name = f'UInt{k4}Col'
    elif kind.startswith('period'):
        col_name = 'Int64Col'
    else:
        kcap = kind.capitalize()
        col_name = f'{kcap}Col'
    return getattr(_tables(), col_name)