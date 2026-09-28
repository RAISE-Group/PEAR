@property
def nbytes(self) -> int:
    n = len(self)
    if n:
        return n * sys.getsizeof(self[0])
    return 0