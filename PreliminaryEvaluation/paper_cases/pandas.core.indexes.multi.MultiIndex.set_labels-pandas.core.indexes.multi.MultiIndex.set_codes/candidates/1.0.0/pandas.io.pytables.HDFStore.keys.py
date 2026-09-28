def keys(self) -> List[str]:
    """
        Return a list of keys corresponding to objects stored in HDFStore.

        Returns
        -------
        list
            List of ABSOLUTE path-names (e.g. have the leading '/').
        """
    return [n._v_pathname for n in self.groups()]