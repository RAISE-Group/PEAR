def test_default_col_names(self):
    result = self.df.melt()
    assert result.columns.tolist() == ['variable', 'value']
    result1 = self.df.melt(id_vars=['id1'])
    assert result1.columns.tolist() == ['id1', 'variable', 'value']
    result2 = self.df.melt(id_vars=['id1', 'id2'])
    assert result2.columns.tolist() == ['id1', 'id2', 'variable', 'value']