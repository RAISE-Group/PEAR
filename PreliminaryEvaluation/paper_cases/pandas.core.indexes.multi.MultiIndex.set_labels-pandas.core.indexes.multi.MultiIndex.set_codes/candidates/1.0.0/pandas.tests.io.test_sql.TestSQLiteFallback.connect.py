@classmethod
def connect(cls):
    return sqlite3.connect(':memory:')