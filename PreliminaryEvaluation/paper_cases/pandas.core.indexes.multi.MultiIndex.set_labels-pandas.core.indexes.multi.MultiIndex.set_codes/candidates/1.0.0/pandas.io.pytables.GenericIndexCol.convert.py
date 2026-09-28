def convert(self, values: np.ndarray, nan_rep, encoding: str, errors: str):
    """
        Convert the data from this selection to the appropriate pandas type.

        Parameters
        ----------
        values : np.ndarray
        nan_rep : str
        encoding : str
        errors : str
        """
    assert isinstance(values, np.ndarray), type(values)
    values = Int64Index(np.arange(len(values)))
    return (values, values)