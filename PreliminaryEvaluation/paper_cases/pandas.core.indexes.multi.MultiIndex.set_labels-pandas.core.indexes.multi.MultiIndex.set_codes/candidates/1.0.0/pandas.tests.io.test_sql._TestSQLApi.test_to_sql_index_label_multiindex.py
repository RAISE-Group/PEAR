def test_to_sql_index_label_multiindex(self):
    temp_frame = DataFrame({'col1': range(4)}, index=MultiIndex.from_product([('A0', 'A1'), ('B0', 'B1')]))
    sql.to_sql(temp_frame, 'test_index_label', self.conn)
    frame = sql.read_sql_query('SELECT * FROM test_index_label', self.conn)
    assert frame.columns[0] == 'level_0'
    assert frame.columns[1] == 'level_1'
    sql.to_sql(temp_frame, 'test_index_label', self.conn, if_exists='replace', index_label=['A', 'B'])
    frame = sql.read_sql_query('SELECT * FROM test_index_label', self.conn)
    assert frame.columns[:2].tolist() == ['A', 'B']
    temp_frame.index.names = ['A', 'B']
    sql.to_sql(temp_frame, 'test_index_label', self.conn, if_exists='replace')
    frame = sql.read_sql_query('SELECT * FROM test_index_label', self.conn)
    assert frame.columns[:2].tolist() == ['A', 'B']
    sql.to_sql(temp_frame, 'test_index_label', self.conn, if_exists='replace', index_label=['C', 'D'])
    frame = sql.read_sql_query('SELECT * FROM test_index_label', self.conn)
    assert frame.columns[:2].tolist() == ['C', 'D']
    msg = "Length of 'index_label' should match number of levels, which is 2"
    with pytest.raises(ValueError, match=msg):
        sql.to_sql(temp_frame, 'test_index_label', self.conn, if_exists='replace', index_label='C')