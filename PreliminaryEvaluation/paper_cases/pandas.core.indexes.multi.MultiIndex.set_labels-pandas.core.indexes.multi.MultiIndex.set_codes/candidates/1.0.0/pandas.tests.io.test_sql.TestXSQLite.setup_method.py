@pytest.fixture(autouse=True)
def setup_method(self, request, datapath):
    self.method = request.function
    self.conn = sqlite3.connect(':memory:')
    yield
    self.method = request.function
    self.conn = sqlite3.connect(':memory:')