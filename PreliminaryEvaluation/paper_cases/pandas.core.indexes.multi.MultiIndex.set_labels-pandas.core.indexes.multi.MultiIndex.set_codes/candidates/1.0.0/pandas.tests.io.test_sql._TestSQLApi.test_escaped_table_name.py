def test_escaped_table_name(self):
    df = DataFrame({'A': [0, 1, 2], 'B': [0.2, np.nan, 5.6]})
    df.to_sql('d1187b08-4943-4c8d-a7f6', self.conn, index=False)
    res = sql.read_sql_query('SELECT * FROM `d1187b08-4943-4c8d-a7f6`', self.conn)
    tm.assert_frame_equal(res, df)