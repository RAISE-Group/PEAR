@tm.network
def test_multiple_matches(self):
    url = 'https://docs.python.org/2/'
    dfs = self.read_html(url, match='Python')
    assert len(dfs) > 1