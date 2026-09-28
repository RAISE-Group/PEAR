@classmethod
def get_atom_string(cls, shape, itemsize):
    return _tables().StringCol(itemsize=itemsize, shape=shape[0])