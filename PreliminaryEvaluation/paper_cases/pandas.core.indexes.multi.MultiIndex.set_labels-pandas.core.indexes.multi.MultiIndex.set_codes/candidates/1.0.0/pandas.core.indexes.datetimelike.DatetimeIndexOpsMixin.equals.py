def equals(self, other) -> bool:
    """
        Determines if two Index objects contain the same elements.
        """
    if self.is_(other):
        return True
    if not isinstance(other, ABCIndexClass):
        return False
    elif not isinstance(other, type(self)):
        try:
            other = type(self)(other)
        except (ValueError, TypeError, OverflowError):
            return False
    if not is_dtype_equal(self.dtype, other.dtype):
        return False
    return np.array_equal(self.asi8, other.asi8)