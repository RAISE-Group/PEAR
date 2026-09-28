def test_works_on_valid_markup(self, datapath):
    filename = datapath('io', 'data', 'html', 'valid_markup.html')
    dfs = self.read_html(filename, index_col=0)
    assert isinstance(dfs, list)
    assert isinstance(dfs[0], DataFrame)