def test_join_on_series(self):
    result = self.target.join(self.source['MergedA'], on='C')
    expected = self.target.join(self.source[['MergedA']], on='C')
    tm.assert_frame_equal(result, expected)