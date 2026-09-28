def test_unstack_level_name(self):
    result = self.frame.unstack('second')
    expected = self.frame.unstack(level=1)
    tm.assert_frame_equal(result, expected)