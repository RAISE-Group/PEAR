def _roundtrip(self):
    self.drop_table('test_frame_roundtrip')
    self.pandasSQL.to_sql(self.test_frame1, 'test_frame_roundtrip')
    result = self.pandasSQL.read_query('SELECT * FROM test_frame_roundtrip')
    result.set_index('level_0', inplace=True)
    result.index.name = None
    tm.assert_frame_equal(result, self.test_frame1)