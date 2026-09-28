def _parse_td(self, row):
    return row.xpath('./td|./th')