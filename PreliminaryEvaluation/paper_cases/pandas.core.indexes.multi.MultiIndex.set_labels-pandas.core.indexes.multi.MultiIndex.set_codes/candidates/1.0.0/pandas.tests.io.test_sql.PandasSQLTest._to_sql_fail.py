def _to_sql_fail(self):
    self.drop_table('test_frame1')
    self.pandasSQL.to_sql(self.test_frame1, 'test_frame1', if_exists='fail')
    assert self.pandasSQL.has_table('test_frame1')
    msg = "Table 'test_frame1' already exists"
    with pytest.raises(ValueError, match=msg):
        self.pandasSQL.to_sql(self.test_frame1, 'test_frame1', if_exists='fail')
    self.drop_table('test_frame1')