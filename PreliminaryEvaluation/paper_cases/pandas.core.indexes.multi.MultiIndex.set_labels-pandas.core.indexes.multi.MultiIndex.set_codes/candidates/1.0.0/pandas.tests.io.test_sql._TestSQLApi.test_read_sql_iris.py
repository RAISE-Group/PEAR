def test_read_sql_iris(self):
    iris_frame = sql.read_sql_query('SELECT * FROM iris', self.conn)
    self._check_iris_loaded_frame(iris_frame)