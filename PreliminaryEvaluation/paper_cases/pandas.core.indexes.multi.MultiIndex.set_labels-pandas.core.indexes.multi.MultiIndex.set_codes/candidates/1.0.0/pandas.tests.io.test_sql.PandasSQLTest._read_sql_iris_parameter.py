def _read_sql_iris_parameter(self):
    query = SQL_STRINGS['read_parameters'][self.flavor]
    params = ['Iris-setosa', 5.1]
    iris_frame = self.pandasSQL.read_query(query, params=params)
    self._check_iris_loaded_frame(iris_frame)