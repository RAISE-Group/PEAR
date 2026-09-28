def test_is_on_offset(self):
    tests = [(BDay(), datetime(2008, 1, 1), True), (BDay(), datetime(2008, 1, 5), False)]
    for offset, d, expected in tests:
        assert_is_on_offset(offset, d, expected)