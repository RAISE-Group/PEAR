def test_sql_open_close(self):
    with tm.ensure_clean() as name:
        conn = self.connect(name)
        sql.to_sql(self.test_frame3, 'test_frame3_legacy', conn, index=False)
        conn.close()
        conn = self.connect(name)
        result = sql.read_sql_query('SELECT * FROM test_frame3_legacy;', conn)
        conn.close()
    tm.assert_frame_equal(self.test_frame3, result)