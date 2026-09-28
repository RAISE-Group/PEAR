@tm.network
def test_python_docs_table(self):
    url = 'https://docs.python.org/2/'
    dfs = self.read_html(url, match='Python')
    zz = [df.iloc[0, 0][0:4] for df in dfs]
    assert sorted(zz) == sorted(['Repo', 'What'])