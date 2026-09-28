def test_constructor_range(self):
    result = DataFrame(range(10))
    expected = DataFrame(list(range(10)))
    tm.assert_frame_equal(result, expected)