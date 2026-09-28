def add_tmp(self, value) -> str:
    """
        Add a temporary variable to the scope.

        Parameters
        ----------
        value : object
            An arbitrary object to be assigned to a temporary variable.

        Returns
        -------
        str
            The name of the temporary variable created.
        """
    name = f'{type(value).__name__}_{self.ntemps}_{_raw_hex_id(self)}'
    assert name not in self.temps
    self.temps[name] = value
    assert name in self.temps
    return name