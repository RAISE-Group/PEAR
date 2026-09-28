@classmethod
def from_array(cls, arr):
    assert isinstance(arr, pa.Array)
    return cls(pa.chunked_array([arr]))