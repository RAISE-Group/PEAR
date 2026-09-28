@classmethod
def setup_driver(cls):
    pymysql = pytest.importorskip('pymysql')
    cls.driver = 'pymysql'
    cls.connect_args = {'client_flag': pymysql.constants.CLIENT.MULTI_STATEMENTS}