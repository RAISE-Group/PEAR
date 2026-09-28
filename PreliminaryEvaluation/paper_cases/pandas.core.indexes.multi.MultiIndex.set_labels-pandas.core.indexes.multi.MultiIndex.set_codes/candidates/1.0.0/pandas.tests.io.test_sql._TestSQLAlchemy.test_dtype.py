def test_dtype(self):
    cols = ['A', 'B']
    data = [(0.8, True), (0.9, None)]
    df = DataFrame(data, columns=cols)
    df.to_sql('dtype_test', self.conn)
    df.to_sql('dtype_test2', self.conn, dtype={'B': sqlalchemy.TEXT})
    meta = sqlalchemy.schema.MetaData(bind=self.conn)
    meta.reflect()
    sqltype = meta.tables['dtype_test2'].columns['B'].type
    assert isinstance(sqltype, sqlalchemy.TEXT)
    msg = 'The type of B is not a SQLAlchemy type'
    with pytest.raises(ValueError, match=msg):
        df.to_sql('error', self.conn, dtype={'B': str})
    df.to_sql('dtype_test3', self.conn, dtype={'B': sqlalchemy.String(10)})
    meta.reflect()
    sqltype = meta.tables['dtype_test3'].columns['B'].type
    assert isinstance(sqltype, sqlalchemy.String)
    assert sqltype.length == 10
    df.to_sql('single_dtype_test', self.conn, dtype=sqlalchemy.TEXT)
    meta = sqlalchemy.schema.MetaData(bind=self.conn)
    meta.reflect()
    sqltypea = meta.tables['single_dtype_test'].columns['A'].type
    sqltypeb = meta.tables['single_dtype_test'].columns['B'].type
    assert isinstance(sqltypea, sqlalchemy.TEXT)
    assert isinstance(sqltypeb, sqlalchemy.TEXT)