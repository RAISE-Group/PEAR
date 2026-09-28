def test_is_on_offset(self):
    tests = []
    tests.append((CustomBusinessHour(start='10:00', end='15:00', holidays=self.holidays), {datetime(2014, 7, 1, 9): False, datetime(2014, 7, 1, 10): True, datetime(2014, 7, 1, 15): True, datetime(2014, 7, 1, 15, 1): False, datetime(2014, 7, 5, 12): False, datetime(2014, 7, 6, 12): False}))
    for offset, cases in tests:
        for dt, expected in cases.items():
            assert offset.is_on_offset(dt) == expected