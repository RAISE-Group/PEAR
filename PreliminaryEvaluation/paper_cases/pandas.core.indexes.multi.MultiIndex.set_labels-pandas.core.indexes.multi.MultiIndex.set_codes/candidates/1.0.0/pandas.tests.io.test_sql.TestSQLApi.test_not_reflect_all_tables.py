def test_not_reflect_all_tables(self):
    qry = 'CREATE TABLE invalid (x INTEGER, y UNKNOWN);'
    self.conn.execute(qry)
    qry = 'CREATE TABLE other_table (x INTEGER, y INTEGER);'
    self.conn.execute(qry)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        sql.read_sql_table('other_table', self.conn)
        sql.read_sql_query('SELECT * FROM other_table', self.conn)
        assert len(w) == 0