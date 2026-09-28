def test_sqlalchemy_type_mapping(self):
    df = DataFrame({'time': to_datetime(['201412120154', '201412110254'], utc=True)})
    db = sql.SQLDatabase(self.conn)
    table = sql.SQLTable('test_type', db, frame=df)
    assert isinstance(table.table.c['time'].type, sqltypes.TIMESTAMP)