def test_database_uri_string(self):
    test_frame1 = self.test_frame1
    with tm.ensure_clean() as name:
        db_uri = 'sqlite:///' + name
        table = 'iris'
        test_frame1.to_sql(table, db_uri, if_exists='replace', index=False)
        test_frame2 = sql.read_sql(table, db_uri)
        test_frame3 = sql.read_sql_table(table, db_uri)
        query = 'SELECT * FROM iris'
        test_frame4 = sql.read_sql_query(query, db_uri)
    tm.assert_frame_equal(test_frame1, test_frame2)
    tm.assert_frame_equal(test_frame1, test_frame3)
    tm.assert_frame_equal(test_frame1, test_frame4)
    try:
        import pg8000
        pytest.skip('pg8000 is installed')
    except ImportError:
        pass
    db_uri = 'postgresql+pg8000://user:pass@host/dbname'
    with pytest.raises(ImportError, match='pg8000'):
        sql.read_sql('select * from table', db_uri)