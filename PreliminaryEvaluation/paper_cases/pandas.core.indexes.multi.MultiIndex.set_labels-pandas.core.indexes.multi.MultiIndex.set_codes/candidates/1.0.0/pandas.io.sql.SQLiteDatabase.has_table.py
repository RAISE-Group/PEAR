def has_table(self, name, schema=None):
    wld = '?'
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name={wld};"
    return len(self.execute(query, [name]).fetchall()) > 0