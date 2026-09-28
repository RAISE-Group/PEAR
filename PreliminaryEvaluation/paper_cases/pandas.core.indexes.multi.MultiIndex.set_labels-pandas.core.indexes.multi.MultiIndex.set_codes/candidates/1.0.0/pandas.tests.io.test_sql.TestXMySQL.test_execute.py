def test_execute(self):
    frame = tm.makeTimeDataFrame()
    drop_sql = 'DROP TABLE IF EXISTS test'
    create_sql = sql.get_schema(frame, 'test')
    cur = self.conn.cursor()
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', 'Unknown table.*')
        cur.execute(drop_sql)
    cur.execute(create_sql)
    ins = 'INSERT INTO test VALUES (%s, %s, %s, %s)'
    row = frame.iloc[0].values.tolist()
    sql.execute(ins, self.conn, params=tuple(row))
    self.conn.commit()
    result = sql.read_sql('select * from test', self.conn)
    result.index = frame.index[:1]
    tm.assert_frame_equal(result, frame[:1])