@classmethod
def get_object(cls, obj, transposed: bool):
    """ these are written transposed """
    if transposed:
        obj = obj.T
    return obj