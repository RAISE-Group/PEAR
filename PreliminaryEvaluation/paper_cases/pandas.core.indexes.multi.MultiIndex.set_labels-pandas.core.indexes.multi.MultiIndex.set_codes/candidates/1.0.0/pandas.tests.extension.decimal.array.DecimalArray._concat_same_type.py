@classmethod
def _concat_same_type(cls, to_concat):
    return cls(np.concatenate([x._data for x in to_concat]))