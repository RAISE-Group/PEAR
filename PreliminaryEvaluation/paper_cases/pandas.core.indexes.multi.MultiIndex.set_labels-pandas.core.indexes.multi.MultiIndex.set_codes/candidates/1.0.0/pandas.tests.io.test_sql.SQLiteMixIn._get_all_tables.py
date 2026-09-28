def _get_all_tables(self):
    c = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return [table[0] for table in c.fetchall()]