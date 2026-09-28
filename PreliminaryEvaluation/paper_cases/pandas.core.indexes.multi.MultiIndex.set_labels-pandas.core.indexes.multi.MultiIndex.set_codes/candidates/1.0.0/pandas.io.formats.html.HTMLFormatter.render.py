def render(self) -> List[str]:
    self._write_table()
    if self.should_show_dimensions:
        by = chr(215)
        self.write('<p>{rows} rows {by} {cols} columns</p>'.format(rows=len(self.frame), by=by, cols=len(self.frame.columns)))
    return self.elements