def _rows_to_cols(self, content):
    col_len = self.num_original_columns
    if self._implicit_index:
        col_len += len(self.index_col)
    max_len = max((len(row) for row in content))
    if max_len > col_len and self.index_col is not False and (self.usecols is None):
        footers = self.skipfooter if self.skipfooter else 0
        bad_lines = []
        iter_content = enumerate(content)
        content_len = len(content)
        content = []
        for i, l in iter_content:
            actual_len = len(l)
            if actual_len > col_len:
                if self.error_bad_lines or self.warn_bad_lines:
                    row_num = self.pos - (content_len - i + footers)
                    bad_lines.append((row_num, actual_len))
                    if self.error_bad_lines:
                        break
            else:
                content.append(l)
        for row_num, actual_len in bad_lines:
            msg = f'Expected {col_len} fields in line {row_num + 1}, saw {actual_len}'
            if self.delimiter and len(self.delimiter) > 1 and (self.quoting != csv.QUOTE_NONE):
                reason = 'Error could possibly be due to quotes being ignored when a multi-char delimiter is used.'
                msg += '. ' + reason
            self._alert_malformed(msg, row_num + 1)
    zipped_content = list(lib.to_object_array(content, min_width=col_len).T)
    if self.usecols:
        if self._implicit_index:
            zipped_content = [a for i, a in enumerate(zipped_content) if i < len(self.index_col) or i - len(self.index_col) in self._col_indices]
        else:
            zipped_content = [a for i, a in enumerate(zipped_content) if i in self._col_indices]
    return zipped_content