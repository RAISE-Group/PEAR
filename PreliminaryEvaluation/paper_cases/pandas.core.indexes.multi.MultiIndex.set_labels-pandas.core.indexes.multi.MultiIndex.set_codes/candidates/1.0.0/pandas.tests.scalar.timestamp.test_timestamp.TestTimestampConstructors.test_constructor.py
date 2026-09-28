def test_constructor(self):
    base_str = '2014-07-01 09:00'
    base_dt = datetime(2014, 7, 1, 9)
    base_expected = 1404205200000000000
    assert calendar.timegm(base_dt.timetuple()) * 1000000000 == base_expected
    tests = [(base_str, base_dt, base_expected), ('2014-07-01 10:00', datetime(2014, 7, 1, 10), base_expected + 3600 * 1000000000), ('2014-07-01 09:00:00.000008000', datetime(2014, 7, 1, 9, 0, 0, 8), base_expected + 8000), ('2014-07-01 09:00:00.000000005', Timestamp('2014-07-01 09:00:00.000000005'), base_expected + 5)]
    timezones = [(None, 0), ('UTC', 0), (pytz.utc, 0), ('Asia/Tokyo', 9), ('US/Eastern', -4), ('dateutil/US/Pacific', -7), (pytz.FixedOffset(-180), -3), (dateutil.tz.tzoffset(None, 18000), 5)]
    for date_str, date, expected in tests:
        for result in [Timestamp(date_str), Timestamp(date)]:
            assert result.value == expected
            assert conversion.pydt_to_i8(result) == expected
            result = Timestamp(result)
            assert result.value == expected
            assert conversion.pydt_to_i8(result) == expected
        for tz, offset in timezones:
            for result in [Timestamp(date_str, tz=tz), Timestamp(date, tz=tz)]:
                expected_tz = expected - offset * 3600 * 1000000000
                assert result.value == expected_tz
                assert conversion.pydt_to_i8(result) == expected_tz
                result = Timestamp(result)
                assert result.value == expected_tz
                assert conversion.pydt_to_i8(result) == expected_tz
                if tz is not None:
                    result = Timestamp(result).tz_convert('UTC')
                else:
                    result = Timestamp(result, tz='UTC')
                expected_utc = expected - offset * 3600 * 1000000000
                assert result.value == expected_utc
                assert conversion.pydt_to_i8(result) == expected_utc