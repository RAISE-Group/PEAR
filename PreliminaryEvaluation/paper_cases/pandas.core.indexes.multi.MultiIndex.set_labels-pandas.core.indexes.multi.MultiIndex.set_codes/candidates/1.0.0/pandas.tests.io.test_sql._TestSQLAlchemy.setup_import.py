@classmethod
def setup_import(cls):
    if not SQLALCHEMY_INSTALLED:
        pytest.skip('SQLAlchemy not installed')