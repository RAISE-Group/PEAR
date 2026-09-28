def _load_iris_view(self):
    self.drop_table('iris_view')
    self._get_exec().execute(SQL_STRINGS['create_view'][self.flavor])