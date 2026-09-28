def test_col_level(self):
    res1 = self.df1.melt(col_level=0)
    res2 = self.df1.melt(col_level='CAP')
    assert res1.columns.tolist() == ['CAP', 'value']
    assert res2.columns.tolist() == ['CAP', 'value']