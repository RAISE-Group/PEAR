def test_custom_var_and_value_name(self):
    result15 = self.df.melt(var_name=self.var_name, value_name=self.value_name)
    assert result15.columns.tolist() == ['var', 'val']
    result16 = self.df.melt(id_vars=['id1'], var_name=self.var_name, value_name=self.value_name)
    assert result16.columns.tolist() == ['id1', 'var', 'val']
    result17 = self.df.melt(id_vars=['id1', 'id2'], var_name=self.var_name, value_name=self.value_name)
    assert result17.columns.tolist() == ['id1', 'id2', 'var', 'val']
    result18 = self.df.melt(id_vars=['id1', 'id2'], value_vars='A', var_name=self.var_name, value_name=self.value_name)
    assert result18.columns.tolist() == ['id1', 'id2', 'var', 'val']
    result19 = self.df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'], var_name=self.var_name, value_name=self.value_name)
    expected19 = DataFrame({'id1': self.df['id1'].tolist() * 2, 'id2': self.df['id2'].tolist() * 2, self.var_name: ['A'] * 10 + ['B'] * 10, self.value_name: self.df['A'].tolist() + self.df['B'].tolist()}, columns=['id1', 'id2', self.var_name, self.value_name])
    tm.assert_frame_equal(result19, expected19)
    df20 = self.df.copy()
    df20.columns.name = 'foo'
    result20 = df20.melt()
    assert result20.columns.tolist() == ['foo', 'value']