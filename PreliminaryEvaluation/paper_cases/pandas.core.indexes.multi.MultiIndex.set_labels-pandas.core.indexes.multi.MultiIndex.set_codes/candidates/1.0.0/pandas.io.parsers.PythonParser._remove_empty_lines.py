def _remove_empty_lines(self, lines):
    """
        Iterate through the lines and remove any that are
        either empty or contain only one whitespace value

        Parameters
        ----------
        lines : array-like
            The array of lines that we are to filter.

        Returns
        -------
        filtered_lines : array-like
            The same array of lines with the "empty" ones removed.
        """
    ret = []
    for l in lines:
        if len(l) > 1 or (len(l) == 1 and (not isinstance(l[0], str) or l[0].strip())):
            ret.append(l)
    return ret