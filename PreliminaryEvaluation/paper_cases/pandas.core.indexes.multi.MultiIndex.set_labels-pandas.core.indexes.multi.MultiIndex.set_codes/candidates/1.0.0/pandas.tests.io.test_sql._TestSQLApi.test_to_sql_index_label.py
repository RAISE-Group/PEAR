@pytest.mark.parametrize('index_name,index_label,expected', [(None, None, 'index'), (None, 'other_label', 'other_label'), ('index_name', None, 'index_name'), ('index_name', 'other_label', 'other_label'), (0, None, '0'), (None, 0, '0')])
def test_to_sql_index_label(self, index_name, index_label, expected):
    temp_frame = DataFrame({'col1': range(4)})
    temp_frame.index.name = index_name
    query = 'SELECT * FROM test_index_label'
    sql.to_sql(temp_frame, 'test_index_label', self.conn, index_label=index_label)
    frame = sql.read_sql_query(query, self.conn)
    assert frame.columns[0] == expected