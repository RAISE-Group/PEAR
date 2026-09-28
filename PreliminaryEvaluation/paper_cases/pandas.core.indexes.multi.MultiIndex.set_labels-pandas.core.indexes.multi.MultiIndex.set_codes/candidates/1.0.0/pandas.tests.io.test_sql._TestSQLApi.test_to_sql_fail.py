def test_to_sql_fail(self):
    sql.to_sql(self.test_frame1, 'test_frame2', self.conn, if_exists='fail')
    assert sql.has_table('test_frame2', self.conn)
    msg = "Table 'test_frame2' already exists"
    with pytest.raises(ValueError, match=msg):
        sql.to_sql(self.test_frame1, 'test_frame2', self.conn, if_exists='fail')