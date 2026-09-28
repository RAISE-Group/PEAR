def test_read_sql_view(self):
    iris_frame = sql.read_sql_query('SELECT * FROM iris_view', self.conn)
    self._check_iris_loaded_frame(iris_frame)