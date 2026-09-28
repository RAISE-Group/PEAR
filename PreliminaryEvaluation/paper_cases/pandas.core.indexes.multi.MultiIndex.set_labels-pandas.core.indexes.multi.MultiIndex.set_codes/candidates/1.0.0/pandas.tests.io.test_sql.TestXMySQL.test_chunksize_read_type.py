def test_chunksize_read_type(self):
    frame = tm.makeTimeDataFrame()
    frame.index.name = 'index'
    drop_sql = 'DROP TABLE IF EXISTS test'
    cur = self.conn.cursor()
    cur.execute(drop_sql)
    sql.to_sql(frame, name='test', con=self.conn)
    query = 'select * from test'
    chunksize = 5
    chunk_gen = pd.read_sql_query(sql=query, con=self.conn, chunksize=chunksize, index_col='index')
    chunk_df = next(chunk_gen)
    tm.assert_frame_equal(frame[:chunksize], chunk_df)