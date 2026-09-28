def write_metadata(self, key: str, values: np.ndarray):
    """
        Write out a metadata array to the key as a fixed-format Series.

        Parameters
        ----------
        key : str
        values : ndarray
        """
    values = Series(values)
    self.parent.put(self._get_metadata_path(key), values, format='table', encoding=self.encoding, errors=self.errors, nan_rep=self.nan_rep)