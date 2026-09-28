@pytest.fixture(autouse=True, scope='class')
def setup_class(cls):
    pymysql = pytest.importorskip('pymysql')
    pymysql.connect(host='localhost', user='root', passwd='', db='pandas_nosetest')
    try:
        pymysql.connect(read_default_group='pandas')
    except pymysql.ProgrammingError:
        raise RuntimeError("Create a group of connection parameters under the heading [pandas] in your system's mysql default file, typically located at ~/.my.cnf or /etc/.my.cnf.")
    except pymysql.Error:
        raise RuntimeError("Cannot connect to database. Create a group of connection parameters under the heading [pandas] in your system's mysql default file, typically located at ~/.my.cnf or /etc/.my.cnf.")