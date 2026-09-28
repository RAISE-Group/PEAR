def _parse_tbody_tr(self, table):
    from_tbody = table.xpath('.//tbody//tr')
    from_root = table.xpath('./tr')
    return from_tbody + from_root