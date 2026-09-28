def _get_exec(self):
    if hasattr(self.conn, 'execute'):
        return self.conn
    else:
        return self.conn.cursor()