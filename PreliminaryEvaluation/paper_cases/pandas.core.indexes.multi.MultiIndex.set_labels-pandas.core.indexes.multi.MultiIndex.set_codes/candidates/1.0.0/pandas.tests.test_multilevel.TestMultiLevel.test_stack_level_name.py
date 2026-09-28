def test_stack_level_name(self):
    unstacked = self.frame.unstack('second')
    result = unstacked.stack('exp')
    expected = self.frame.unstack().stack(0)
    tm.assert_frame_equal(result, expected)
    result = self.frame.stack('exp')
    expected = self.frame.stack()
    tm.assert_series_equal(result, expected)