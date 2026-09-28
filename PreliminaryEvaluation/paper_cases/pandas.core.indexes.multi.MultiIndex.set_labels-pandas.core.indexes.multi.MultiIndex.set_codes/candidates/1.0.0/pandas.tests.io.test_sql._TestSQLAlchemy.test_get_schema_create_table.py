def test_get_schema_create_table(self):
    self._load_test3_data()
    tbl = 'test_get_schema_create_table'
    create_sql = sql.get_schema(self.test_frame3, tbl, con=self.conn)
    blank_test_df = self.test_frame3.iloc[:0]
    self.drop_table(tbl)
    self.conn.execute(create_sql)
    returned_df = sql.read_sql_table(tbl, self.conn)
    tm.assert_frame_equal(returned_df, blank_test_df, check_index_type=False)
    self.drop_table(tbl)