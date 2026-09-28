def test_read_table_columns(self):
    sql.to_sql(self.test_frame1, 'test_frame', self.conn)
    cols = ['A', 'B']
    result = sql.read_sql_table('test_frame', self.conn, columns=cols)
    assert result.columns.tolist() == cols