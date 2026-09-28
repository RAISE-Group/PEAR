def test_bigint(self):
    df = DataFrame(data={'i64': [2 ** 62]})
    df.to_sql('test_bigint', self.conn, index=False)
    result = sql.read_sql_table('test_bigint', self.conn)
    tm.assert_frame_equal(df, result)