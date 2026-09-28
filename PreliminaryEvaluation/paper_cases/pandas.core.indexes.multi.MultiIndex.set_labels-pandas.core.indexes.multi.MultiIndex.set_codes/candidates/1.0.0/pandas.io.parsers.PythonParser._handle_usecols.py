def _handle_usecols(self, columns, usecols_key):
    """
        Sets self._col_indices

        usecols_key is used if there are string usecols.
        """
    if self.usecols is not None:
        if callable(self.usecols):
            col_indices = _evaluate_usecols(self.usecols, usecols_key)
        elif any((isinstance(u, str) for u in self.usecols)):
            if len(columns) > 1:
                raise ValueError('If using multiple headers, usecols must be integers.')
            col_indices = []
            for col in self.usecols:
                if isinstance(col, str):
                    try:
                        col_indices.append(usecols_key.index(col))
                    except ValueError:
                        _validate_usecols_names(self.usecols, usecols_key)
                else:
                    col_indices.append(col)
        else:
            col_indices = self.usecols
        columns = [[n for i, n in enumerate(column) if i in col_indices] for column in columns]
        self._col_indices = col_indices
    return columns