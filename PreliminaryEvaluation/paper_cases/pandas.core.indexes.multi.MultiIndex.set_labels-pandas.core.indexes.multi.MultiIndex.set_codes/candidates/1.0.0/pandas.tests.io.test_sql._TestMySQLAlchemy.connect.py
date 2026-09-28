@classmethod
def connect(cls):
    url = 'mysql+{driver}://root@localhost/pandas_nosetest'
    return sqlalchemy.create_engine(url.format(driver=cls.driver), connect_args=cls.connect_args)