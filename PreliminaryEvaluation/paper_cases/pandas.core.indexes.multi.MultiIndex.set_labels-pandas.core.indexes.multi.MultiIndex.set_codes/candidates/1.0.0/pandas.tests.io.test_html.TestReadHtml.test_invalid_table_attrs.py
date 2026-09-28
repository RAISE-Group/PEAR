@pytest.mark.slow
def test_invalid_table_attrs(self):
    url = self.banklist_data
    with pytest.raises(ValueError, match='No tables found'):
        self.read_html(url, 'First Federal Bank of Florida', attrs={'id': 'tasdfable'})