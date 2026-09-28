@pytest.fixture(autouse=True)
def setup_method(self, load_iris_data):
    self.load_test_data_and_sql()