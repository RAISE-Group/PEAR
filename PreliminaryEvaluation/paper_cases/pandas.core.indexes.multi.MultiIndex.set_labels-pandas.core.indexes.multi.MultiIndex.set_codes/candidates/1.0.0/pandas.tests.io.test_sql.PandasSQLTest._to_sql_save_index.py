def _to_sql_save_index(self):
    df = DataFrame.from_records([(1, 2.1, 'line1'), (2, 1.5, 'line2')], columns=['A', 'B', 'C'], index=['A'])
    self.pandasSQL.to_sql(df, 'test_to_sql_saves_index')
    ix_cols = self._get_index_columns('test_to_sql_saves_index')
    assert ix_cols == [['A']]