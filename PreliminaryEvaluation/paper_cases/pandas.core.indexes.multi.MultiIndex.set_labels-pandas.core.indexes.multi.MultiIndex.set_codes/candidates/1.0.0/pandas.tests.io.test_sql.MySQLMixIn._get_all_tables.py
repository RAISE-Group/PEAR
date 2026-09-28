def _get_all_tables(self):
    cur = self.conn.cursor()
    cur.execute('SHOW TABLES')
    return [table[0] for table in cur.fetchall()]