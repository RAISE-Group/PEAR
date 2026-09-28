def has_table(self, name, schema=None):
    return self.connectable.run_callable(self.connectable.dialect.has_table, name, schema or self.meta.schema)