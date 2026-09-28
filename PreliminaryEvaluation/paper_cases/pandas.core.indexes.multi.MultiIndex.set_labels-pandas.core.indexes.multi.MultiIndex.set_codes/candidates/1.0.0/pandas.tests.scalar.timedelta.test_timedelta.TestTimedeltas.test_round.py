def test_round(self):
    t1 = Timedelta('1 days 02:34:56.789123456')
    t2 = Timedelta('-1 days 02:34:56.789123456')
    for freq, s1, s2 in [('N', t1, t2), ('U', Timedelta('1 days 02:34:56.789123000'), Timedelta('-1 days 02:34:56.789123000')), ('L', Timedelta('1 days 02:34:56.789000000'), Timedelta('-1 days 02:34:56.789000000')), ('S', Timedelta('1 days 02:34:57'), Timedelta('-1 days 02:34:57')), ('2S', Timedelta('1 days 02:34:56'), Timedelta('-1 days 02:34:56')), ('5S', Timedelta('1 days 02:34:55'), Timedelta('-1 days 02:34:55')), ('T', Timedelta('1 days 02:35:00'), Timedelta('-1 days 02:35:00')), ('12T', Timedelta('1 days 02:36:00'), Timedelta('-1 days 02:36:00')), ('H', Timedelta('1 days 03:00:00'), Timedelta('-1 days 03:00:00')), ('d', Timedelta('1 days'), Timedelta('-1 days'))]:
        r1 = t1.round(freq)
        assert r1 == s1
        r2 = t2.round(freq)
        assert r2 == s2
    for freq, msg in [('Y', '<YearEnd: month=12> is a non-fixed frequency'), ('M', '<MonthEnd> is a non-fixed frequency'), ('foobar', 'Invalid frequency: foobar')]:
        with pytest.raises(ValueError, match=msg):
            t1.round(freq)
    t1 = timedelta_range('1 days', periods=3, freq='1 min 2 s 3 us')
    t2 = -1 * t1
    t1a = timedelta_range('1 days', periods=3, freq='1 min 2 s')
    t1c = TimedeltaIndex([1, 1, 1], unit='D')
    for freq, s1, s2 in [('N', t1, t2), ('U', t1, t2), ('L', t1a, TimedeltaIndex(['-1 days +00:00:00', '-2 days +23:58:58', '-2 days +23:57:56'], dtype='timedelta64[ns]', freq=None)), ('S', t1a, TimedeltaIndex(['-1 days +00:00:00', '-2 days +23:58:58', '-2 days +23:57:56'], dtype='timedelta64[ns]', freq=None)), ('12T', t1c, TimedeltaIndex(['-1 days', '-1 days', '-1 days'], dtype='timedelta64[ns]', freq=None)), ('H', t1c, TimedeltaIndex(['-1 days', '-1 days', '-1 days'], dtype='timedelta64[ns]', freq=None)), ('d', t1c, TimedeltaIndex([-1, -1, -1], unit='D'))]:
        r1 = t1.round(freq)
        tm.assert_index_equal(r1, s1)
        r2 = t2.round(freq)
        tm.assert_index_equal(r2, s2)
    for freq, msg in [('Y', '<YearEnd: month=12> is a non-fixed frequency'), ('M', '<MonthEnd> is a non-fixed frequency'), ('foobar', 'Invalid frequency: foobar')]:
        with pytest.raises(ValueError, match=msg):
            t1.round(freq)