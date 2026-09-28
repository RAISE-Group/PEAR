def variable_labels(self):
    """
        Return variable labels as a dict, associating each variable name
        with corresponding label.

        Returns
        -------
        dict
        """
    return dict(zip(self.varlist, self._variable_labels))