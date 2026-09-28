def test_constructor_iterator(self):
    result = DataFrame(iter(range(10)))
    expected = DataFrame(list(range(10)))
    tm.assert_frame_equal(result, expected)