@pytest.mark.slow
def test_thousands_macau_stats(self, datapath):
    all_non_nan_table_index = -2
    macau_data = datapath('io', 'data', 'html', 'macau.html')
    dfs = self.read_html(macau_data, index_col=0, attrs={'class': 'style1'})
    df = dfs[all_non_nan_table_index]
    assert not any((s.isna().any() for _, s in df.items()))