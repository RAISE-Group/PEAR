def test_date_parsing(self):
    df = sql.read_sql_query('SELECT * FROM types_test_data', self.conn)
    assert not issubclass(df.DateCol.dtype.type, np.datetime64)
    df = sql.read_sql_query('SELECT * FROM types_test_data', self.conn, parse_dates=['DateCol'])
    assert issubclass(df.DateCol.dtype.type, np.datetime64)
    assert df.DateCol.tolist() == [pd.Timestamp(2000, 1, 3, 0, 0, 0), pd.Timestamp(2000, 1, 4, 0, 0, 0)]
    df = sql.read_sql_query('SELECT * FROM types_test_data', self.conn, parse_dates={'DateCol': '%Y-%m-%d %H:%M:%S'})
    assert issubclass(df.DateCol.dtype.type, np.datetime64)
    assert df.DateCol.tolist() == [pd.Timestamp(2000, 1, 3, 0, 0, 0), pd.Timestamp(2000, 1, 4, 0, 0, 0)]
    df = sql.read_sql_query('SELECT * FROM types_test_data', self.conn, parse_dates=['IntDateCol'])
    assert issubclass(df.IntDateCol.dtype.type, np.datetime64)
    assert df.IntDateCol.tolist() == [pd.Timestamp(1986, 12, 25, 0, 0, 0), pd.Timestamp(2013, 1, 1, 0, 0, 0)]
    df = sql.read_sql_query('SELECT * FROM types_test_data', self.conn, parse_dates={'IntDateCol': 's'})
    assert issubclass(df.IntDateCol.dtype.type, np.datetime64)
    assert df.IntDateCol.tolist() == [pd.Timestamp(1986, 12, 25, 0, 0, 0), pd.Timestamp(2013, 1, 1, 0, 0, 0)]
    df = sql.read_sql_query('SELECT * FROM types_test_data', self.conn, parse_dates={'IntDateOnlyCol': '%Y%m%d'})
    assert issubclass(df.IntDateOnlyCol.dtype.type, np.datetime64)
    assert df.IntDateOnlyCol.tolist() == [pd.Timestamp('2010-10-10'), pd.Timestamp('2010-12-12')]