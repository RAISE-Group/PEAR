def test_write_row_by_row(self):
    frame = tm.makeTimeDataFrame()
    frame.iloc[0, 0] = np.nan
    drop_sql = 'DROP TABLE IF EXISTS test'
    create_sql = sql.get_schema(frame, 'test')
    cur = self.conn.cursor()
    cur.execute(drop_sql)
    cur.execute(create_sql)
    ins = 'INSERT INTO test VALUES (%s, %s, %s, %s)'
    for idx, row in frame.iterrows():
        fmt_sql = format_query(ins, *row)
        tquery(fmt_sql, cur=cur)
    self.conn.commit()
    result = sql.read_sql('select * from test', con=self.conn)
    result.index = frame.index
    tm.assert_frame_equal(result, frame, check_less_precise=True)