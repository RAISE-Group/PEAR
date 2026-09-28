def test_default_date_load(self):
    df = sql.read_sql_table('types_test_data', self.conn)
    assert not issubclass(df.DateCol.dtype.type, np.datetime64)