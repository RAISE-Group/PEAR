@classmethod
def connect(cls):
    url = 'postgresql+{driver}://postgres@localhost/pandas_nosetest'
    return sqlalchemy.create_engine(url.format(driver=cls.driver))