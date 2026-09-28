def _parse_tbody_tr(self, table):
    from_tbody = table.select('tbody tr')
    from_root = table.find_all('tr', recursive=False)
    return from_tbody + from_root