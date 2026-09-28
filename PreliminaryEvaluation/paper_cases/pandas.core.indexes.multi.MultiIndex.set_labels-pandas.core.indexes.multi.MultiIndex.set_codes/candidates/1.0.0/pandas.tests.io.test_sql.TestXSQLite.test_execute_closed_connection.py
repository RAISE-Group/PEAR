def test_execute_closed_connection(self):
    create_sql = '\n        CREATE TABLE test\n        (\n        a TEXT,\n        b TEXT,\n        c REAL,\n        PRIMARY KEY (a, b)\n        );\n        '
    cur = self.conn.cursor()
    cur.execute(create_sql)
    sql.execute('INSERT INTO test VALUES("foo", "bar", 1.234)', self.conn)
    self.conn.close()
    with pytest.raises(Exception):
        tquery('select * from test', con=self.conn)