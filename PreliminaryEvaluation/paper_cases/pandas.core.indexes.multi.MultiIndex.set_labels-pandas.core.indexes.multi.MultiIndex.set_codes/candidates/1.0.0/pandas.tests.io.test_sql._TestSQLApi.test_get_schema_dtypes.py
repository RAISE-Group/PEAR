def test_get_schema_dtypes(self):
    float_frame = DataFrame({'a': [1.1, 1.2], 'b': [2.1, 2.2]})
    dtype = sqlalchemy.Integer if self.mode == 'sqlalchemy' else 'INTEGER'
    create_sql = sql.get_schema(float_frame, 'test', con=self.conn, dtype={'b': dtype})
    assert 'CREATE' in create_sql
    assert 'INTEGER' in create_sql