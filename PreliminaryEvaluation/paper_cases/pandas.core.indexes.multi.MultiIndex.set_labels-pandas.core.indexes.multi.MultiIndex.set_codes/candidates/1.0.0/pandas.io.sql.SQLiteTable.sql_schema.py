def sql_schema(self):
    return str(';\n'.join(self.table))