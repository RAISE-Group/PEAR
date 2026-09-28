def get_chunk(self, size=None):
    """
        Reads lines from Xport file and returns as dataframe

        Parameters
        ----------
        size : int, defaults to None
            Number of lines to read.  If None, reads whole file.

        Returns
        -------
        DataFrame
        """
    if size is None:
        size = self._chunksize
    return self.read(nrows=size)