def test_execute_fail(self):
    create_sql = '\n        CREATE TABLE test\n        (\n        a TEXT,\n        b TEXT,\n        c REAL,\n        PRIMARY KEY (a, b)\n        );\n        '
    cur = self.conn.cursor()
    cur.execute(create_sql)
    sql.execute('INSERT INTO test VALUES("foo", "bar", 1.234)', self.conn)
    sql.execute('INSERT INTO test VALUES("foo", "baz", 2.567)', self.conn)
    with pytest.raises(Exception):
        sql.execute('INSERT INTO test VALUES("foo", "bar", 7)', self.conn)