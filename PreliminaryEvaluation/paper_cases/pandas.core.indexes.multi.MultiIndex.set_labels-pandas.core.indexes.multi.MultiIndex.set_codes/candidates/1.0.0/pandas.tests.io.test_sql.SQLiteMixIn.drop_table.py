def drop_table(self, table_name):
    self.conn.execute(f'DROP TABLE IF EXISTS {sql._get_valid_sqlite_name(table_name)}')
    self.conn.commit()