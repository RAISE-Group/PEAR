def test_value_vars_types(self):
    expected = DataFrame({'id1': self.df['id1'].tolist() * 2, 'id2': self.df['id2'].tolist() * 2, 'variable': ['A'] * 10 + ['B'] * 10, 'value': self.df['A'].tolist() + self.df['B'].tolist()}, columns=['id1', 'id2', 'variable', 'value'])
    for type_ in (tuple, list, np.array):
        result = self.df.melt(id_vars=['id1', 'id2'], value_vars=type_(('A', 'B')))
        tm.assert_frame_equal(result, expected)