def test_nanosecond_string_parsing(self):
    ts = Timestamp('2013-05-01 07:15:45.123456789')
    expected_repr = '2013-05-01 07:15:45.123456789'
    expected_value = 1367392545123456789
    assert ts.value == expected_value
    assert expected_repr in repr(ts)
    ts = Timestamp('2013-05-01 07:15:45.123456789+09:00', tz='Asia/Tokyo')
    assert ts.value == expected_value - 9 * 3600 * 1000000000
    assert expected_repr in repr(ts)
    ts = Timestamp('2013-05-01 07:15:45.123456789', tz='UTC')
    assert ts.value == expected_value
    assert expected_repr in repr(ts)
    ts = Timestamp('2013-05-01 07:15:45.123456789', tz='US/Eastern')
    assert ts.value == expected_value + 4 * 3600 * 1000000000
    assert expected_repr in repr(ts)
    ts = Timestamp('20130501T071545.123456789')
    assert ts.value == expected_value
    assert expected_repr in repr(ts)