def _read_sql_iris(self):
    iris_frame = self.pandasSQL.read_query('SELECT * FROM iris')
    self._check_iris_loaded_frame(iris_frame)