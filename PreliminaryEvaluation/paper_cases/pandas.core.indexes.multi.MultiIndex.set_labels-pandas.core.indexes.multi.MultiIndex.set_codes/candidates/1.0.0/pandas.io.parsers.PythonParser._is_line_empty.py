def _is_line_empty(self, line):
    """
        Check if a line is empty or not.

        Parameters
        ----------
        line : str, array-like
            The line of data to check.

        Returns
        -------
        boolean : Whether or not the line is empty.
        """
    return not line or all((not x for x in line))