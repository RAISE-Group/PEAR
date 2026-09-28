@pytest.mark.slow
def test_banklist(self):
    df1 = self.read_html(self.banklist_data, '.*Florida.*', attrs={'id': 'table'})
    df2 = self.read_html(self.banklist_data, 'Metcalf Bank', attrs={'id': 'table'})
    assert_framelist_equal(df1, df2)