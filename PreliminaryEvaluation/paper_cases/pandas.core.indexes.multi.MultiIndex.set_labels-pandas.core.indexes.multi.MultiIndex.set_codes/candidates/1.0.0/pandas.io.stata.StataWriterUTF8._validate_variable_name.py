def _validate_variable_name(self, name: str) -> str:
    """
        Validate variable names for Stata export.

        Parameters
        ----------
        name : str
            Variable name

        Returns
        -------
        str
            The validated name with invalid characters replaced with
            underscores.

        Notes
        -----
        Stata 118+ support most unicode characters. The only limitation is in
        the ascii range where the characters supported are a-z, A-Z, 0-9 and _.
        """
    for c in name:
        if ord(c) < 128 and (c < 'A' or c > 'Z') and (c < 'a' or c > 'z') and (c < '0' or c > '9') and (c != '_') or 128 <= ord(c) < 256:
            name = name.replace(c, '_')
    return name