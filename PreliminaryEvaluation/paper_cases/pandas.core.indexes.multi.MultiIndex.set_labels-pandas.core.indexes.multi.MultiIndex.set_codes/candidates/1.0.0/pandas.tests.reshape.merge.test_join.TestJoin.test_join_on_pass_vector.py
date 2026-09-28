def test_join_on_pass_vector(self):
    expected = self.target.join(self.source, on='C')
    del expected['C']
    join_col = self.target.pop('C')
    result = self.target.join(self.source, on=join_col)
    tm.assert_frame_equal(result, expected)