@pytest.mark.skipif(SQLALCHEMY_INSTALLED, reason='SQLAlchemy is installed')
def test_con_string_import_error(self):
    conn = 'mysql://root@localhost/pandas_nosetest'
    msg = 'Using URI string without sqlalchemy installed'
    with pytest.raises(ImportError, match=msg):
        sql.read_sql('SELECT * FROM iris', conn)