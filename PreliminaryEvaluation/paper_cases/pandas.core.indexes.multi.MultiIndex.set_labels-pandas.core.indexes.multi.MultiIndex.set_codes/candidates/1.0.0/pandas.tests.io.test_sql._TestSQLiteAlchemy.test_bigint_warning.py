def test_bigint_warning(self):
    df = DataFrame({'a': [1, 2]}, dtype='int64')
    df.to_sql('test_bigintwarning', self.conn, index=False)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        sql.read_sql_table('test_bigintwarning', self.conn)
        assert len(w) == 0