@classmethod
def get_atom_datetime64(cls, shape):
    return _tables().Int64Col(shape=shape[0])