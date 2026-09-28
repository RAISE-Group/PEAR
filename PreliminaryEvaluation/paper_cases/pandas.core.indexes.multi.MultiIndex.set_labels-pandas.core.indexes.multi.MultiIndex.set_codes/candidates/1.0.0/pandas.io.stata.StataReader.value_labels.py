def value_labels(self):
    """
        Return a dict, associating each variable name a dict, associating
        each value its corresponding label.

        Returns
        -------
        dict
        """
    if not self._value_labels_read:
        self._read_value_labels()
    return self.value_label_dict