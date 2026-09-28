@pytest.fixture(autouse=True, scope='class')
def setup_class(cls):
    cls.setup_import()
    cls.setup_driver()
    conn = cls.connect()
    conn.connect()