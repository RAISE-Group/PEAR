def drop_table(self, table_name, schema=None):
    schema = schema or self.meta.schema
    if self.has_table(table_name, schema):
        self.meta.reflect(only=[table_name], schema=schema)
        self.get_table(table_name, schema).drop()
        self.meta.clear()