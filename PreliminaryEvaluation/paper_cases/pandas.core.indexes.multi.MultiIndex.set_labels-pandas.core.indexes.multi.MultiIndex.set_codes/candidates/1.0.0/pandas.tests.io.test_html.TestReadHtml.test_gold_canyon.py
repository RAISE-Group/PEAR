@pytest.mark.slow
def test_gold_canyon(self):
    gc = 'Gold Canyon'
    with open(self.banklist_data, 'r') as f:
        raw_text = f.read()
    assert gc in raw_text
    df = self.read_html(self.banklist_data, 'Gold Canyon', attrs={'id': 'table'})[0]
    assert gc in df.to_string()