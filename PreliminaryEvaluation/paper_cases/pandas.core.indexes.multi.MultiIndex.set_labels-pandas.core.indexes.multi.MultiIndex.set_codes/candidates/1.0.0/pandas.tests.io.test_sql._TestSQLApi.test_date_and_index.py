def test_date_and_index(self):
    df = sql.read_sql_query('SELECT * FROM types_test_data', self.conn, index_col='DateCol', parse_dates=['DateCol', 'IntDateCol'])
    assert issubclass(df.index.dtype.type, np.datetime64)
    assert issubclass(df.IntDateCol.dtype.type, np.datetime64)