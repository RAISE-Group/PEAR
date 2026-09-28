def test_read_table(self):
    iris_frame = sql.read_sql_table('iris', con=self.conn)
    self._check_iris_loaded_frame(iris_frame)