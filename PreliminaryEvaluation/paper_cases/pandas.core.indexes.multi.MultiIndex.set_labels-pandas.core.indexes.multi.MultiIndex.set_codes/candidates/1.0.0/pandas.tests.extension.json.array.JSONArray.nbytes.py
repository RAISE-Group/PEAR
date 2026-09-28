@property
def nbytes(self) -> int:
    return sys.getsizeof(self.data)