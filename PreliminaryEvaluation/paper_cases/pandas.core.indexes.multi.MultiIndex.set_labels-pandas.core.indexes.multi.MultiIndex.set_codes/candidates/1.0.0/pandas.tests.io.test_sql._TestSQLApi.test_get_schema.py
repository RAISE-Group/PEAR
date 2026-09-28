def test_get_schema(self):
    create_sql = sql.get_schema(self.test_frame1, 'test', con=self.conn)
    assert 'CREATE' in create_sql