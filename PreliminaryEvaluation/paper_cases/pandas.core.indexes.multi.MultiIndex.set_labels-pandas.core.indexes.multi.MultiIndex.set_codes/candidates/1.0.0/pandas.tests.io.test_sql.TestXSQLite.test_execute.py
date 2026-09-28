def test_execute(self):
    frame = tm.makeTimeDataFrame()
    create_sql = sql.get_schema(frame, 'test')
    cur = self.conn.cursor()
    cur.execute(create_sql)
    ins = 'INSERT INTO test VALUES (?, ?, ?, ?)'
    row = frame.iloc[0]
    sql.execute(ins, self.conn, params=tuple(row))
    self.conn.commit()
    result = sql.read_sql('select * from test', self.conn)
    result.index = frame.index[:1]
    tm.assert_frame_equal(result, frame[:1])