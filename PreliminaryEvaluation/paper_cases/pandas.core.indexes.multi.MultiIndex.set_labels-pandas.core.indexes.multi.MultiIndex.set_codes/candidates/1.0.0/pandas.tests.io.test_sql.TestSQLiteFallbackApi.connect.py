def connect(self, database=':memory:'):
    return sqlite3.connect(database)