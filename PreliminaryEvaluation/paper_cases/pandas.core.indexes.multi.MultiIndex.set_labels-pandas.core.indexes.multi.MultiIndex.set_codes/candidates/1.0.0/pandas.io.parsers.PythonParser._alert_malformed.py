def _alert_malformed(self, msg, row_num):
    """
        Alert a user about a malformed row.

        If `self.error_bad_lines` is True, the alert will be `ParserError`.
        If `self.warn_bad_lines` is True, the alert will be printed out.

        Parameters
        ----------
        msg : The error message to display.
        row_num : The row number where the parsing error occurred.
                  Because this row number is displayed, we 1-index,
                  even though we 0-index internally.
        """
    if self.error_bad_lines:
        raise ParserError(msg)
    elif self.warn_bad_lines:
        base = f'Skipping line {row_num}: '
        sys.stderr.write(base + msg + '\n')