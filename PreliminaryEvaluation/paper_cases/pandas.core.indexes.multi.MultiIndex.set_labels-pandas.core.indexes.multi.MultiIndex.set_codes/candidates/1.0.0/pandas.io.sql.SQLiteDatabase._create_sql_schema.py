def _create_sql_schema(self, frame, table_name, keys=None, dtype=None):
    table = SQLiteTable(table_name, self, frame=frame, index=False, keys=keys, dtype=dtype)
    return str(table.sql_schema())