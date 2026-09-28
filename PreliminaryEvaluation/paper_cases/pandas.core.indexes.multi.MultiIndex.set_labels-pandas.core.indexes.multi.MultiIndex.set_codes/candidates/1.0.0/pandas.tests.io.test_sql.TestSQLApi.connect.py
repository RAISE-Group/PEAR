def connect(self):
    return sqlalchemy.create_engine('sqlite:///:memory:')