def load_test_data_and_sql(self):
    self.pandasSQL = sql.SQLiteDatabase(self.conn)
    self._load_test1_data()