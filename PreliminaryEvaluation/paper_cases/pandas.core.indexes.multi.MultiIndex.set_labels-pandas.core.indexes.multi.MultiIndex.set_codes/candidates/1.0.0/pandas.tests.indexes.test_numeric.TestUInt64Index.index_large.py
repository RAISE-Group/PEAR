@pytest.fixture
def index_large(self):
    large = [2 ** 63, 2 ** 63 + 10, 2 ** 63 + 15, 2 ** 63 + 20, 2 ** 63 + 25]
    return UInt64Index(large)