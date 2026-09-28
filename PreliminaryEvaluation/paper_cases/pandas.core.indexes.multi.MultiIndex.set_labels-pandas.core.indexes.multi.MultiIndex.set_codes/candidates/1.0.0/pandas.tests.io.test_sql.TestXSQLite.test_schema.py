def test_schema(self):
    frame = tm.makeTimeDataFrame()
    create_sql = sql.get_schema(frame, 'test')
    lines = create_sql.splitlines()
    for l in lines:
        tokens = l.split(' ')
        if len(tokens) == 2 and tokens[0] == 'A':
            assert tokens[1] == 'DATETIME'
    frame = tm.makeTimeDataFrame()
    create_sql = sql.get_schema(frame, 'test', keys=['A', 'B'])
    lines = create_sql.splitlines()
    assert 'PRIMARY KEY ("A", "B")' in create_sql
    cur = self.conn.cursor()
    cur.execute(create_sql)