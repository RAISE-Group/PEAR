def test_pass_function(self):
    result = self.data.pivot_table('D', index=lambda x: x // 5, columns=self.data.C)
    expected = self.data.pivot_table('D', index=self.data.index // 5, columns='C')
    tm.assert_frame_equal(result, expected)