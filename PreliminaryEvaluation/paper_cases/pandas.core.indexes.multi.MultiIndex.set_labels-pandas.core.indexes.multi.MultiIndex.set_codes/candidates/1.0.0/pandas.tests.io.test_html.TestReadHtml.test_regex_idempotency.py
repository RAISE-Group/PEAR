@pytest.mark.slow
def test_regex_idempotency(self):
    url = self.banklist_data
    dfs = self.read_html(file_path_to_url(os.path.abspath(url)), match=re.compile(re.compile('Florida')), attrs={'id': 'table'})
    assert isinstance(dfs, list)
    for df in dfs:
        assert isinstance(df, DataFrame)