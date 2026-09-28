@classmethod
def _concat_same_type(cls, to_concat):
    data = np.concatenate([x.data for x in to_concat])
    return cls(data)