def _next_iter_line(self, row_num):
    """
        Wrapper around iterating through `self.data` (CSV source).

        When a CSV error is raised, we check for specific
        error messages that allow us to customize the
        error message displayed to the user.

        Parameters
        ----------
        row_num : The row number of the line being parsed.
        """
    try:
        return next(self.data)
    except csv.Error as e:
        if self.warn_bad_lines or self.error_bad_lines:
            msg = str(e)
            if 'NULL byte' in msg or 'line contains NUL' in msg:
                msg = "NULL byte detected. This byte cannot be processed in Python's native csv library at the moment, so please pass in engine='c' instead"
            if self.skipfooter > 0:
                reason = "Error could possibly be due to parsing errors in the skipped footer rows (the skipfooter keyword is only applied after Python's csv library has parsed all rows)."
                msg += '. ' + reason
            self._alert_malformed(msg, row_num)
        return None