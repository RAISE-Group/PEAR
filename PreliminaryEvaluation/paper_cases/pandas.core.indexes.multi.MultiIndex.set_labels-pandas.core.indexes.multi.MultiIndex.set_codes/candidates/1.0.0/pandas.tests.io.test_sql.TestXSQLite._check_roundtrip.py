def _check_roundtrip(self, frame):
    sql.to_sql(frame, name='test_table', con=self.conn, index=False)
    result = sql.read_sql('select * from test_table', self.conn)
    result.index = frame.index
    expected = frame
    tm.assert_frame_equal(result, expected)
    frame['txt'] = ['a'] * len(frame)
    frame2 = frame.copy()
    new_idx = Index(np.arange(len(frame2))) + 10
    frame2['Idx'] = new_idx.copy()
    sql.to_sql(frame2, name='test_table2', con=self.conn, index=False)
    result = sql.read_sql('select * from test_table2', self.conn, index_col='Idx')
    expected = frame.copy()
    expected.index = new_idx
    expected.index.name = 'Idx'
    tm.assert_frame_equal(expected, result)