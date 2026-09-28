def test_custom_value_name(self):
    result10 = self.df.melt(value_name=self.value_name)
    assert result10.columns.tolist() == ['variable', 'val']
    result11 = self.df.melt(id_vars=['id1'], value_name=self.value_name)
    assert result11.columns.tolist() == ['id1', 'variable', 'val']
    result12 = self.df.melt(id_vars=['id1', 'id2'], value_name=self.value_name)
    assert result12.columns.tolist() == ['id1', 'id2', 'variable', 'val']
    result13 = self.df.melt(id_vars=['id1', 'id2'], value_vars='A', value_name=self.value_name)
    assert result13.columns.tolist() == ['id1', 'id2', 'variable', 'val']
    result14 = self.df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'], value_name=self.value_name)
    expected14 = DataFrame({'id1': self.df['id1'].tolist() * 2, 'id2': self.df['id2'].tolist() * 2, 'variable': ['A'] * 10 + ['B'] * 10, self.value_name: self.df['A'].tolist() + self.df['B'].tolist()}, columns=['id1', 'id2', 'variable', self.value_name])
    tm.assert_frame_equal(result14, expected14)