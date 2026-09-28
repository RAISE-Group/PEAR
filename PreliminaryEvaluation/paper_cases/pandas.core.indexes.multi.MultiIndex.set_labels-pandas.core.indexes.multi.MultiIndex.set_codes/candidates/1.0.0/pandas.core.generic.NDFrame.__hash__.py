def __hash__(self):
    raise TypeError(f'{repr(type(self).__name__)} objects are mutable, thus they cannot be hashed')