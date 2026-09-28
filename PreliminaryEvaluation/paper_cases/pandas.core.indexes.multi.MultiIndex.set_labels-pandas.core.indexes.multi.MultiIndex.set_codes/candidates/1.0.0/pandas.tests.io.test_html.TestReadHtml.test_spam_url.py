@tm.network
def test_spam_url(self):
    url = 'https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/io/data/html/spam.html'
    df1 = self.read_html(url, '.*Water.*')
    df2 = self.read_html(url, 'Unit')
    assert_framelist_equal(df1, df2)