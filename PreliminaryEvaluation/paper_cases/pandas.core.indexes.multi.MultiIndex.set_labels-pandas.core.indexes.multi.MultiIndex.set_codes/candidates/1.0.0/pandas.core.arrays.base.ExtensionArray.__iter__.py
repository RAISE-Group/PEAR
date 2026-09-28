def __iter__(self):
    """
        Iterate over elements of the array.
        """
    for i in range(len(self)):
        yield self[i]