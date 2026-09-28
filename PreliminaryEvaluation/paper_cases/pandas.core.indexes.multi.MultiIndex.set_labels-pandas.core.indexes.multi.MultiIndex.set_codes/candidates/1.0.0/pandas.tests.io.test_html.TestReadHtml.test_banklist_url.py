@tm.network
def test_banklist_url(self):
    url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
    df1 = self.read_html(url, 'First Federal Bank of Florida', attrs={'id': 'table'})
    df2 = self.read_html(url, 'Metcalf Bank', attrs={'id': 'table'})
    assert_framelist_equal(df1, df2)