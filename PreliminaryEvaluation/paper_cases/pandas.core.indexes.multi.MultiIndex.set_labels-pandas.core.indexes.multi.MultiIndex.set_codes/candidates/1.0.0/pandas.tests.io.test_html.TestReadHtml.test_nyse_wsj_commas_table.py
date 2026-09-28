def test_nyse_wsj_commas_table(self, datapath):
    data = datapath('io', 'data', 'html', 'nyse_wsj.html')
    df = self.read_html(data, index_col=0, header=0, attrs={'class': 'mdcTable'})[0]
    expected = Index(['Issue(Roll over for charts and headlines)', 'Volume', 'Price', 'Chg', '% Chg'])
    nrows = 100
    assert df.shape[0] == nrows
    tm.assert_index_equal(df.columns, expected)