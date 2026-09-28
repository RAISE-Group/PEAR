def test_resolution(self):

    def _assert_less(ts1, ts2):
        val1 = self.dtc.convert(ts1, None, None)
        val2 = self.dtc.convert(ts2, None, None)
        if not val1 < val2:
            raise AssertionError(f'{val1} is not less than {val2}.')
    ts = Timestamp('2012-1-1')
    _assert_less(ts, ts + Second())
    _assert_less(ts, ts + Milli())
    _assert_less(ts, ts + Micro(50))