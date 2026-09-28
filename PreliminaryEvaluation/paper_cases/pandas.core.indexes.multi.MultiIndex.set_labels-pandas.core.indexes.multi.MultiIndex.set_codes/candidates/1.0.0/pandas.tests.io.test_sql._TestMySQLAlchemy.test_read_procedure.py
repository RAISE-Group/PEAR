def test_read_procedure(self):
    import pymysql
    df = DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3]})
    df.to_sql('test_procedure', self.conn, index=False)
    proc = 'DROP PROCEDURE IF EXISTS get_testdb;\n\n        CREATE PROCEDURE get_testdb ()\n\n        BEGIN\n            SELECT * FROM test_procedure;\n        END'
    connection = self.conn.connect()
    trans = connection.begin()
    try:
        r1 = connection.execute(proc)
        trans.commit()
    except pymysql.Error:
        trans.rollback()
        raise
    res1 = sql.read_sql_query('CALL get_testdb();', self.conn)
    tm.assert_frame_equal(df, res1)
    res2 = sql.read_sql('CALL get_testdb();', self.conn)
    tm.assert_frame_equal(df, res2)