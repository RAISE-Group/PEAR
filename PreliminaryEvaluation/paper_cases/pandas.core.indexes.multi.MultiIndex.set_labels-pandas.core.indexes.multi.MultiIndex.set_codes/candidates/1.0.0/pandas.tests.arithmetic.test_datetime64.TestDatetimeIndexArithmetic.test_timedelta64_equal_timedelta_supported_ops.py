@pytest.mark.parametrize('op', [operator.add, operator.sub])
def test_timedelta64_equal_timedelta_supported_ops(self, op):
    ser = Series([Timestamp('20130301'), Timestamp('20130228 23:00:00'), Timestamp('20130228 22:00:00'), Timestamp('20130228 21:00:00')])
    intervals = ['D', 'h', 'm', 's', 'us']

    def timedelta64(*args):
        return np.sum(list(starmap(np.timedelta64, zip(args, intervals))))
    for d, h, m, s, us in product(*[range(2)] * 5):
        nptd = timedelta64(d, h, m, s, us)
        pytd = timedelta(days=d, hours=h, minutes=m, seconds=s, microseconds=us)
        lhs = op(ser, nptd)
        rhs = op(ser, pytd)
        tm.assert_series_equal(lhs, rhs)