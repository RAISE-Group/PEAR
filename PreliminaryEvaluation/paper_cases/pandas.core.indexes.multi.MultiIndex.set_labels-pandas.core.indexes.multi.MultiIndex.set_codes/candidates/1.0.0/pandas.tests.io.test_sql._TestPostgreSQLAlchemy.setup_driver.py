@classmethod
def setup_driver(cls):
    pytest.importorskip('psycopg2')
    cls.driver = 'psycopg2'