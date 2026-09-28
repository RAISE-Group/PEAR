def teardown_method(self, method):
    if hasattr(self, 'conn'):
        for tbl in self._get_all_tables():
            self.drop_table(tbl)
        self._close_conn()