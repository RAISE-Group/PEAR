def _get_sqlite_column_type(self, schema, column):
    for col in schema.split('\n'):
        if col.split()[0].strip('""') == column:
            return col.split()[1]
    raise ValueError(f'Column {column} not found')