def _bank_data(self, *args, **kwargs):
    return self.read_html(self.banklist_data, 'Metcalf', *args, attrs={'id': 'table'}, **kwargs)