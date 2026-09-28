def drop_table(self, name, schema=None):
    drop_sql = f'DROP TABLE {_get_valid_sqlite_name(name)}'
    self.execute(drop_sql)