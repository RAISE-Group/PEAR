def test_get_schema2(self):
    create_sql = sql.get_schema(self.test_frame1, 'test')
    assert 'CREATE' in create_sql