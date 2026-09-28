def test_vars_work_with_multiindex(self):
    expected = DataFrame({('A', 'a'): self.df1['A', 'a'], 'CAP': ['B'] * len(self.df1), 'low': ['b'] * len(self.df1), 'value': self.df1['B', 'b']}, columns=[('A', 'a'), 'CAP', 'low', 'value'])
    result = self.df1.melt(id_vars=[('A', 'a')], value_vars=[('B', 'b')])
    tm.assert_frame_equal(result, expected)