def test_banklist_no_match(self):
    dfs = self.read_html(self.banklist_data, attrs={'id': 'table'})
    for df in dfs:
        assert isinstance(df, DataFrame)