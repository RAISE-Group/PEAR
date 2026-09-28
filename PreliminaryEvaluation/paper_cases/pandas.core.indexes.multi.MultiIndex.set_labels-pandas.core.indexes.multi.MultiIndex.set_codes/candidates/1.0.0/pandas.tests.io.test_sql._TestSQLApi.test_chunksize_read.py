def test_chunksize_read(self):
    df = DataFrame(np.random.randn(22, 5), columns=list('abcde'))
    df.to_sql('test_chunksize', self.conn, index=False)
    res1 = sql.read_sql_query('select * from test_chunksize', self.conn)
    res2 = DataFrame()
    i = 0
    sizes = [5, 5, 5, 5, 2]
    for chunk in sql.read_sql_query('select * from test_chunksize', self.conn, chunksize=5):
        res2 = concat([res2, chunk], ignore_index=True)
        assert len(chunk) == sizes[i]
        i += 1
    tm.assert_frame_equal(res1, res2)
    if self.mode == 'sqlalchemy':
        res3 = DataFrame()
        i = 0
        sizes = [5, 5, 5, 5, 2]
        for chunk in sql.read_sql_table('test_chunksize', self.conn, chunksize=5):
            res3 = concat([res3, chunk], ignore_index=True)
            assert len(chunk) == sizes[i]
            i += 1
        tm.assert_frame_equal(res1, res3)