def test_pivot_table_multiple(self):
    index = ['A', 'B']
    columns = 'C'
    table = pivot_table(self.data, index=index, columns=columns)
    expected = self.data.groupby(index + [columns]).agg(np.mean).unstack()
    tm.assert_frame_equal(table, expected)