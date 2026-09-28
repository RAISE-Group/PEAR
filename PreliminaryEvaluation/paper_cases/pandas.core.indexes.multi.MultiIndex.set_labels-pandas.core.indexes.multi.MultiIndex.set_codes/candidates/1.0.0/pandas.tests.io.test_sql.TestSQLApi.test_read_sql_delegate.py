def test_read_sql_delegate(self):
    iris_frame1 = sql.read_sql_query('SELECT * FROM iris', self.conn)
    iris_frame2 = sql.read_sql('SELECT * FROM iris', self.conn)
    tm.assert_frame_equal(iris_frame1, iris_frame2)
    iris_frame1 = sql.read_sql_table('iris', self.conn)
    iris_frame2 = sql.read_sql('iris', self.conn)
    tm.assert_frame_equal(iris_frame1, iris_frame2)