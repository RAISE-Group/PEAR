@pytest.fixture(autouse=True)
def setup_method(self, load_iris_data):
    super().load_test_data_and_sql()
    engine = self.conn
    conn = engine.connect()
    self.__tx = conn.begin()
    self.pandasSQL = sql.SQLDatabase(conn)
    self.__engine = engine
    self.conn = conn
    yield
    self.__tx.rollback()
    self.conn.close()
    self.conn = self.__engine
    self.pandasSQL = sql.SQLDatabase(self.__engine)