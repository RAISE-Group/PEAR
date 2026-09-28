def test_custom_var_name(self):
    result5 = self.df.melt(var_name=self.var_name)
    assert result5.columns.tolist() == ['var', 'value']
    result6 = self.df.melt(id_vars=['id1'], var_name=self.var_name)
    assert result6.columns.tolist() == ['id1', 'var', 'value']
    result7 = self.df.melt(id_vars=['id1', 'id2'], var_name=self.var_name)
    assert result7.columns.tolist() == ['id1', 'id2', 'var', 'value']
    result8 = self.df.melt(id_vars=['id1', 'id2'], value_vars='A', var_name=self.var_name)
    assert result8.columns.tolist() == ['id1', 'id2', 'var', 'value']
    result9 = self.df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'], var_name=self.var_name)
    expected9 = DataFrame({'id1': self.df['id1'].tolist() * 2, 'id2': self.df['id2'].tolist() * 2, self.var_name: ['A'] * 10 + ['B'] * 10, 'value': self.df['A'].tolist() + self.df['B'].tolist()}, columns=['id1', 'id2', self.var_name, 'value'])
    tm.assert_frame_equal(result9, expected9)