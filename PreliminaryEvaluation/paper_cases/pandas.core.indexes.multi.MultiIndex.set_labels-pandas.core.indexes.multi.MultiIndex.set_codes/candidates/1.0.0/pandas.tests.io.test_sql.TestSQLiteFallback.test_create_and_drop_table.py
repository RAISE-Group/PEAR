def test_create_and_drop_table(self):
    temp_frame = DataFrame({'one': [1.0, 2.0, 3.0, 4.0], 'two': [4.0, 3.0, 2.0, 1.0]})
    self.pandasSQL.to_sql(temp_frame, 'drop_test_frame')
    assert self.pandasSQL.has_table('drop_test_frame')
    self.pandasSQL.drop_table('drop_test_frame')
    assert not self.pandasSQL.has_table('drop_test_frame')