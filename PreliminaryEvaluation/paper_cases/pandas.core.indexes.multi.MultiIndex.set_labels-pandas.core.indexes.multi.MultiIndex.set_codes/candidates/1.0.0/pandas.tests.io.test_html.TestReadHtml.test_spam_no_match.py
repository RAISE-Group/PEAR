def test_spam_no_match(self):
    dfs = self.read_html(self.spam_data)
    for df in dfs:
        assert isinstance(df, DataFrame)