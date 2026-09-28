def _parse_thead_tr(self, table):
    rows = []
    for thead in table.xpath('.//thead'):
        rows.extend(thead.xpath('./tr'))
        elements_at_root = thead.xpath('./td|./th')
        if elements_at_root:
            rows.append(thead)
    return rows