def _parse_tables(self, doc, match, kwargs):
    pattern = match.pattern
    xpath_expr = f'//table//*[re:test(text(), {repr(pattern)})]/ancestor::table'
    if kwargs:
        xpath_expr += _build_xpath_expr(kwargs)
    tables = doc.xpath(xpath_expr, namespaces=_re_namespace)
    tables = self._handle_hidden_tables(tables, 'attrib')
    if self.displayed_only:
        for table in tables:
            for elem in table.xpath('.//*[@style]'):
                if 'display:none' in elem.attrib.get('style', '').replace(' ', ''):
                    elem.getparent().remove(elem)
    if not tables:
        raise ValueError(f'No tables found matching regex {repr(pattern)}')
    return tables