@classmethod
def from_scalars(cls, values):
    arr = pa.chunked_array([pa.array(np.asarray(values))])
    return cls(arr)