def test_pass_array(self):
    result = self.data.pivot_table('D', index=self.data.A, columns=self.data.C)
    expected = self.data.pivot_table('D', index='A', columns='C')
    tm.assert_frame_equal(result, expected)