def test_sqlite_type_mapping(self):
    df = DataFrame({'time': to_datetime(['201412120154', '201412110254'], utc=True)})
    db = sql.SQLiteDatabase(self.conn)
    table = sql.SQLiteTable('test_type', db, frame=df)
    schema = table.sql_schema()
    assert self._get_sqlite_column_type(schema, 'time') == 'TIMESTAMP'