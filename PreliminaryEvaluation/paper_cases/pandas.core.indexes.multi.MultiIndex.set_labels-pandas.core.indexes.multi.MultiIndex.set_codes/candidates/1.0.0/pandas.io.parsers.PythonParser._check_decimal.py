def _check_decimal(self, lines):
    if self.decimal == _parser_defaults['decimal']:
        return lines
    return self._search_replace_num_columns(lines=lines, search=self.decimal, replace='.')