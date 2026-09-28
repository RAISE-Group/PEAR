def _get_sqlite_column_type(self, table, column):
    recs = self.conn.execute(f'PRAGMA table_info({table})')
    for cid, name, ctype, not_null, default, pk in recs:
        if name == column:
            return ctype
    raise ValueError(f'Table {table}, column {column} not found')