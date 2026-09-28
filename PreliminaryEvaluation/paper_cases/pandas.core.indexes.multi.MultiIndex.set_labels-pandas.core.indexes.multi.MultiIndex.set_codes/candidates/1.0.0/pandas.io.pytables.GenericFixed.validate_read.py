def validate_read(self, columns, where):
    """
        raise if any keywords are passed which are not-None
        """
    if columns is not None:
        raise TypeError('cannot pass a column specification when reading a Fixed format store. this store must be selected in its entirety')
    if where is not None:
        raise TypeError('cannot pass a where specification when reading from a Fixed format store. this store must be selected in its entirety')