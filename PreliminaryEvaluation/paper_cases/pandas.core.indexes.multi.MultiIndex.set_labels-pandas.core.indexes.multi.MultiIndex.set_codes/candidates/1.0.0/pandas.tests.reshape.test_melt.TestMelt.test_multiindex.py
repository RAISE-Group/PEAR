def test_multiindex(self):
    res = self.df1.melt()
    assert res.columns.tolist() == ['CAP', 'low', 'value']