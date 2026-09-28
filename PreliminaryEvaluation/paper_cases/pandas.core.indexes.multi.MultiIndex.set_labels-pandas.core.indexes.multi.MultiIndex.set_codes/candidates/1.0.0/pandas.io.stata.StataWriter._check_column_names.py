def _check_column_names(self, data):
    """
        Checks column names to ensure that they are valid Stata column names.
        This includes checks for:
            * Non-string names
            * Stata keywords
            * Variables that start with numbers
            * Variables with names that are too long

        When an illegal variable name is detected, it is converted, and if
        dates are exported, the variable name is propagated to the date
        conversion dictionary
        """
    converted_names = {}
    columns = list(data.columns)
    original_columns = columns[:]
    duplicate_var_id = 0
    for j, name in enumerate(columns):
        orig_name = name
        if not isinstance(name, str):
            name = str(name)
        name = self._validate_variable_name(name)
        if name in self.RESERVED_WORDS:
            name = '_' + name
        if name[0] >= '0' and name[0] <= '9':
            name = '_' + name
        name = name[:min(len(name), 32)]
        if not name == orig_name:
            while columns.count(name) > 0:
                name = '_' + str(duplicate_var_id) + name
                name = name[:min(len(name), 32)]
                duplicate_var_id += 1
            converted_names[orig_name] = name
        columns[j] = name
    data.columns = columns
    if self._convert_dates:
        for c, o in zip(columns, original_columns):
            if c != o:
                self._convert_dates[c] = self._convert_dates[o]
                del self._convert_dates[o]
    if converted_names:
        conversion_warning = []
        for orig_name, name in converted_names.items():
            try:
                orig_name = orig_name.encode('utf-8')
            except (UnicodeDecodeError, AttributeError):
                pass
            msg = f'{orig_name}   ->   {name}'
            conversion_warning.append(msg)
        ws = invalid_name_doc.format('\n    '.join(conversion_warning))
        warnings.warn(ws, InvalidColumnName)
    self._converted_names = converted_names
    self._update_strl_names()
    return data