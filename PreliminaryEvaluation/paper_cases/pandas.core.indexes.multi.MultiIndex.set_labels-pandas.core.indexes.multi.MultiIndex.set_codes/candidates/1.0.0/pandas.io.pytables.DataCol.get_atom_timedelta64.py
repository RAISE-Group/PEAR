@classmethod
def get_atom_timedelta64(cls, shape):
    return _tables().Int64Col(shape=shape[0])