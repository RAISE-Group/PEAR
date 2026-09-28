@classmethod
def connect(cls):
    return sqlalchemy.create_engine('sqlite:///:memory:')