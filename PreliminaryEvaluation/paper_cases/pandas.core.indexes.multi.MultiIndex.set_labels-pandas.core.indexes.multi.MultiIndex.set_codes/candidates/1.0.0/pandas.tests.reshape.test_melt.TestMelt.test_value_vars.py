def test_value_vars(self):
    result3 = self.df.melt(id_vars=['id1', 'id2'], value_vars='A')
    assert len(result3) == 10
    result4 = self.df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'])
    expected4 = DataFrame({'id1': self.df['id1'].tolist() * 2, 'id2': self.df['id2'].tolist() * 2, 'variable': ['A'] * 10 + ['B'] * 10, 'value': self.df['A'].tolist() + self.df['B'].tolist()}, columns=['id1', 'id2', 'variable', 'value'])
    tm.assert_frame_equal(result4, expected4)