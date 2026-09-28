def test_dtype(self):
    if self.flavor == 'mysql':
        pytest.skip('Not applicable to MySQL legacy')
    cols = ['A', 'B']
    data = [(0.8, True), (0.9, None)]
    df = DataFrame(data, columns=cols)
    df.to_sql('dtype_test', self.conn)
    df.to_sql('dtype_test2', self.conn, dtype={'B': 'STRING'})
    assert self._get_sqlite_column_type('dtype_test', 'B') == 'INTEGER'
    assert self._get_sqlite_column_type('dtype_test2', 'B') == 'STRING'
    msg = "B \\(<class 'bool'>\\) not a string"
    with pytest.raises(ValueError, match=msg):
        df.to_sql('error', self.conn, dtype={'B': bool})
    df.to_sql('single_dtype_test', self.conn, dtype='STRING')
    assert self._get_sqlite_column_type('single_dtype_test', 'A') == 'STRING'
    assert self._get_sqlite_column_type('single_dtype_test', 'B') == 'STRING'