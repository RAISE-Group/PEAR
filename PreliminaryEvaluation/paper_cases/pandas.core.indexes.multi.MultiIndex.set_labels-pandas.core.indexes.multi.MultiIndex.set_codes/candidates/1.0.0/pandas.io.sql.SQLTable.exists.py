def exists(self):
    return self.pd_sql.has_table(self.name, self.schema)