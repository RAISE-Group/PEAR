def _check_roundtrip(self, frame):
    drop_sql = 'DROP TABLE IF EXISTS test_table'
    cur = self.conn.cursor()
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', 'Unknown table.*')
        cur.execute(drop_sql)
    sql.to_sql(frame, name='test_table', con=self.conn, index=False)
    result = sql.read_sql('select * from test_table', self.conn)
    result.index = frame.index
    result.index.name = frame.index.name
    expected = frame
    tm.assert_frame_equal(result, expected)
    frame['txt'] = ['a'] * len(frame)
    frame2 = frame.copy()
    index = Index(np.arange(len(frame2))) + 10
    frame2['Idx'] = index
    drop_sql = 'DROP TABLE IF EXISTS test_table2'
    cur = self.conn.cursor()
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', 'Unknown table.*')
        cur.execute(drop_sql)
    sql.to_sql(frame2, name='test_table2', con=self.conn, index=False)
    result = sql.read_sql('select * from test_table2', self.conn, index_col='Idx')
    expected = frame.copy()
    expected.index = index
    expected.index.names = result.index.names
    tm.assert_frame_equal(expected, result)