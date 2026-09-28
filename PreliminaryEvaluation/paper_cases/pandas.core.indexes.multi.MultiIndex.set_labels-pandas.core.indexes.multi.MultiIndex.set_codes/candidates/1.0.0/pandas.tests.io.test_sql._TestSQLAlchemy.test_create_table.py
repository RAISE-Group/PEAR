def test_create_table(self):
    temp_conn = self.connect()
    temp_frame = DataFrame({'one': [1.0, 2.0, 3.0, 4.0], 'two': [4.0, 3.0, 2.0, 1.0]})
    pandasSQL = sql.SQLDatabase(temp_conn)
    pandasSQL.to_sql(temp_frame, 'temp_frame')
    assert temp_conn.has_table('temp_frame')