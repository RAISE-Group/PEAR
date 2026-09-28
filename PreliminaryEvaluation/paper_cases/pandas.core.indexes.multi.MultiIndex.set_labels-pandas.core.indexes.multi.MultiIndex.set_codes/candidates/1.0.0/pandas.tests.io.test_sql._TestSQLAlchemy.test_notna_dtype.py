def test_notna_dtype(self):
    cols = {'Bool': Series([True, None]), 'Date': Series([datetime(2012, 5, 1), None]), 'Int': Series([1, None], dtype='object'), 'Float': Series([1.1, None])}
    df = DataFrame(cols)
    tbl = 'notna_dtype_test'
    df.to_sql(tbl, self.conn)
    returned_df = sql.read_sql_table(tbl, self.conn)
    meta = sqlalchemy.schema.MetaData(bind=self.conn)
    meta.reflect()
    if self.flavor == 'mysql':
        my_type = sqltypes.Integer
    else:
        my_type = sqltypes.Boolean
    col_dict = meta.tables[tbl].columns
    assert isinstance(col_dict['Bool'].type, my_type)
    assert isinstance(col_dict['Date'].type, sqltypes.DateTime)
    assert isinstance(col_dict['Int'].type, sqltypes.Integer)
    assert isinstance(col_dict['Float'].type, sqltypes.Float)