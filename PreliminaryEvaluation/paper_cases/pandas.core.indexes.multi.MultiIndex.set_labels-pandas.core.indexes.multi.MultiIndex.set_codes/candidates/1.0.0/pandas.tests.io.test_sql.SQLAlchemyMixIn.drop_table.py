def drop_table(self, table_name):
    sql.SQLDatabase(self.conn).drop_table(table_name)