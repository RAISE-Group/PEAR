def setup_connect(self):
    try:
        self.conn = self.connect()
        self.pandasSQL = sql.SQLDatabase(self.conn)
        self.conn.connect()
    except sqlalchemy.exc.OperationalError:
        pytest.skip(f"Can't connect to {self.flavor} server")