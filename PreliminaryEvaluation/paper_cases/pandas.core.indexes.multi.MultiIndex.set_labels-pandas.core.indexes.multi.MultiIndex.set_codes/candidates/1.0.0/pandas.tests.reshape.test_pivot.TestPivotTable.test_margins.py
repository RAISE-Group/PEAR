def test_margins(self):

    def _check_output(result, values_col, index=['A', 'B'], columns=['C'], margins_col='All'):
        col_margins = result.loc[result.index[:-1], margins_col]
        expected_col_margins = self.data.groupby(index)[values_col].mean()
        tm.assert_series_equal(col_margins, expected_col_margins, check_names=False)
        assert col_margins.name == margins_col
        result = result.sort_index()
        index_margins = result.loc[margins_col, ''].iloc[:-1]
        expected_ix_margins = self.data.groupby(columns)[values_col].mean()
        tm.assert_series_equal(index_margins, expected_ix_margins, check_names=False)
        assert index_margins.name == (margins_col, '')
        grand_total_margins = result.loc[(margins_col, ''), margins_col]
        expected_total_margins = self.data[values_col].mean()
        assert grand_total_margins == expected_total_margins
    result = self.data.pivot_table(values='D', index=['A', 'B'], columns='C', margins=True, aggfunc=np.mean)
    _check_output(result, 'D')
    result = self.data.pivot_table(values='D', index=['A', 'B'], columns='C', margins=True, aggfunc=np.mean, margins_name='Totals')
    _check_output(result, 'D', margins_col='Totals')
    table = self.data.pivot_table(index=['A', 'B'], columns='C', margins=True, aggfunc=np.mean)
    for value_col in table.columns.levels[0]:
        _check_output(table[value_col], value_col)
    self.data.columns = [k * 2 for k in self.data.columns]
    table = self.data.pivot_table(index=['AA', 'BB'], margins=True, aggfunc=np.mean)
    for value_col in table.columns:
        totals = table.loc[('All', ''), value_col]
        assert totals == self.data[value_col].mean()
    rtable = self.data.pivot_table(columns=['AA', 'BB'], margins=True, aggfunc=np.mean)
    assert isinstance(rtable, Series)
    table = self.data.pivot_table(index=['AA', 'BB'], margins=True, aggfunc='mean')
    for item in ['DD', 'EE', 'FF']:
        totals = table.loc[('All', ''), item]
        assert totals == self.data[item].mean()