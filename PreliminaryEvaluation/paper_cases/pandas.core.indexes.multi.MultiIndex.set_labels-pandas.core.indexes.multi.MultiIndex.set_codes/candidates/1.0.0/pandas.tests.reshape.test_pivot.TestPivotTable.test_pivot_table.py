def test_pivot_table(self, observed):
    index = ['A', 'B']
    columns = 'C'
    table = pivot_table(self.data, values='D', index=index, columns=columns, observed=observed)
    table2 = self.data.pivot_table(values='D', index=index, columns=columns, observed=observed)
    tm.assert_frame_equal(table, table2)
    pivot_table(self.data, values='D', index=index, observed=observed)
    if len(index) > 1:
        assert table.index.names == tuple(index)
    else:
        assert table.index.name == index[0]
    if len(columns) > 1:
        assert table.columns.names == columns
    else:
        assert table.columns.name == columns[0]
    expected = self.data.groupby(index + [columns])['D'].agg(np.mean).unstack()
    tm.assert_frame_equal(table, expected)