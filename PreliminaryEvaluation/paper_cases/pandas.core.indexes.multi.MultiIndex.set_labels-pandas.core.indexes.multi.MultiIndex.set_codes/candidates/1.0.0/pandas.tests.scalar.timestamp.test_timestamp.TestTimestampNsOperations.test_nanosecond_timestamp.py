def test_nanosecond_timestamp(self):
    expected = 1293840000000000005
    t = Timestamp('2011-01-01') + offsets.Nano(5)
    assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
    assert t.value == expected
    assert t.nanosecond == 5
    t = Timestamp(t)
    assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
    assert t.value == expected
    assert t.nanosecond == 5
    t = Timestamp(np_datetime64_compat('2011-01-01 00:00:00.000000005Z'))
    assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
    assert t.value == expected
    assert t.nanosecond == 5
    expected = 1293840000000000010
    t = t + offsets.Nano(5)
    assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000010')"
    assert t.value == expected
    assert t.nanosecond == 10
    t = Timestamp(t)
    assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000010')"
    assert t.value == expected
    assert t.nanosecond == 10
    t = Timestamp(np_datetime64_compat('2011-01-01 00:00:00.000000010Z'))
    assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000010')"
    assert t.value == expected
    assert t.nanosecond == 10