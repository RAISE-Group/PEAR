def _format_body(self):
    if isinstance(self.df.index, ABCMultiIndex):
        return self._format_hierarchical_rows()
    else:
        return self._format_regular_rows()