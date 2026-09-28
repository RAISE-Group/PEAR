def test_double_precision(self):
    V = 1.2345678910111213
    df = DataFrame({'f32': Series([V], dtype='float32'), 'f64': Series([V], dtype='float64'), 'f64_as_f32': Series([V], dtype='float64'), 'i32': Series([5], dtype='int32'), 'i64': Series([5], dtype='int64')})
    df.to_sql('test_dtypes', self.conn, index=False, if_exists='replace', dtype={'f64_as_f32': sqlalchemy.Float(precision=23)})
    res = sql.read_sql_table('test_dtypes', self.conn)
    assert np.round(df['f64'].iloc[0], 14) == np.round(res['f64'].iloc[0], 14)
    meta = sqlalchemy.schema.MetaData(bind=self.conn)
    meta.reflect()
    col_dict = meta.tables['test_dtypes'].columns
    assert str(col_dict['f32'].type) == str(col_dict['f64_as_f32'].type)
    assert isinstance(col_dict['f32'].type, sqltypes.Float)
    assert isinstance(col_dict['f64'].type, sqltypes.Float)
    assert isinstance(col_dict['i32'].type, sqltypes.Integer)
    assert isinstance(col_dict['i64'].type, sqltypes.BigInteger)