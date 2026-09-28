@pytest.mark.slow
def test_thousands_macau_index_col(self, datapath, request):
    if self.read_html.keywords.get('flavor') == 'bs4' and td.safe_import('bs4', '4.8.0'):
        reason = 'fails for bs4 version >= 4.8.0'
        request.node.add_marker(pytest.mark.xfail(reason=reason))
    all_non_nan_table_index = -2
    macau_data = datapath('io', 'data', 'html', 'macau.html')
    dfs = self.read_html(macau_data, index_col=0, header=0)
    df = dfs[all_non_nan_table_index]
    assert not any((s.isna().any() for _, s in df.items()))