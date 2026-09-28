def test_fields(self):

    def check(value, equal):
        assert isinstance(value, int)
        assert value == equal
    ts = Timestamp('2015-05-10 09:06:03.000100001')
    check(ts.year, 2015)
    check(ts.month, 5)
    check(ts.day, 10)
    check(ts.hour, 9)
    check(ts.minute, 6)
    check(ts.second, 3)
    msg = "'Timestamp' object has no attribute 'millisecond'"
    with pytest.raises(AttributeError, match=msg):
        ts.millisecond
    check(ts.microsecond, 100)
    check(ts.nanosecond, 1)
    check(ts.dayofweek, 6)
    check(ts.quarter, 2)
    check(ts.dayofyear, 130)
    check(ts.week, 19)
    check(ts.daysinmonth, 31)
    check(ts.daysinmonth, 31)
    ts = Timestamp('2014-12-31 23:59:00-05:00', tz='US/Eastern')
    check(ts.year, 2014)
    check(ts.month, 12)
    check(ts.day, 31)
    check(ts.hour, 23)
    check(ts.minute, 59)
    check(ts.second, 0)
    msg = "'Timestamp' object has no attribute 'millisecond'"
    with pytest.raises(AttributeError, match=msg):
        ts.millisecond
    check(ts.microsecond, 0)
    check(ts.nanosecond, 0)
    check(ts.dayofweek, 2)
    check(ts.quarter, 4)
    check(ts.dayofyear, 365)
    check(ts.week, 1)
    check(ts.daysinmonth, 31)
    ts = Timestamp('2014-01-01 00:00:00+01:00')
    starts = ['is_month_start', 'is_quarter_start', 'is_year_start']
    for start in starts:
        assert getattr(ts, start)
    ts = Timestamp('2014-12-31 23:59:59+01:00')
    ends = ['is_month_end', 'is_year_end', 'is_quarter_end']
    for end in ends:
        assert getattr(ts, end)