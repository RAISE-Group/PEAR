def _write_table(self, indent: int=0) -> None:
    _classes = ['dataframe']
    use_mathjax = get_option('display.html.use_mathjax')
    if not use_mathjax:
        _classes.append('tex2jax_ignore')
    if self.classes is not None:
        if isinstance(self.classes, str):
            self.classes = self.classes.split()
        if not isinstance(self.classes, (list, tuple)):
            raise TypeError('classes must be a string, list, or tuple, not {typ}'.format(typ=type(self.classes)))
        _classes.extend(self.classes)
    if self.table_id is None:
        id_section = ''
    else:
        id_section = ' id="{table_id}"'.format(table_id=self.table_id)
    self.write('<table border="{border}" class="{cls}"{id_section}>'.format(border=self.border, cls=' '.join(_classes), id_section=id_section), indent)
    if self.fmt.header or self.show_row_idx_names:
        self._write_header(indent + self.indent_delta)
    self._write_body(indent + self.indent_delta)
    self.write('</table>', indent)