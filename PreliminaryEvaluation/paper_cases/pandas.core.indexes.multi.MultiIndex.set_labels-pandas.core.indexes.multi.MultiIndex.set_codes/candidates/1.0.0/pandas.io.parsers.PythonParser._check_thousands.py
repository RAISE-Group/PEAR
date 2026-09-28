def _check_thousands(self, lines):
    if self.thousands is None:
        return lines
    return self._search_replace_num_columns(lines=lines, search=self.thousands, replace='')