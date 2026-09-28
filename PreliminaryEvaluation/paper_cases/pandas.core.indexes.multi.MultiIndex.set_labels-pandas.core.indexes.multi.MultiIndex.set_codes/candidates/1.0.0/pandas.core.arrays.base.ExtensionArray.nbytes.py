@property
def nbytes(self) -> int:
    """
        The number of bytes needed to store this object in memory.
        """
    raise AbstractMethodError(self)