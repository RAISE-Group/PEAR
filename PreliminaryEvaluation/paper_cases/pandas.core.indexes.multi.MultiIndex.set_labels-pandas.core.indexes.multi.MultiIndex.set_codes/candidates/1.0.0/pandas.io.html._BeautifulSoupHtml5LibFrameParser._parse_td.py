def _parse_td(self, row):
    return row.find_all(('td', 'th'), recursive=False)