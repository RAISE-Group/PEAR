def drop_table(self, table_name):
    cur = self.conn.cursor()
    cur.execute(f'DROP TABLE IF EXISTS {sql._get_valid_mysql_name(table_name)}')
    self.conn.commit()