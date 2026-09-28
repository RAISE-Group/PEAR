def test_roundtrip(self):
    base = Timestamp('20140101 00:00:00')
    result = Timestamp(base.value + Timedelta('5ms').value)
    assert result == Timestamp(f'{base}.005000')
    assert result.microsecond == 5000
    result = Timestamp(base.value + Timedelta('5us').value)
    assert result == Timestamp(f'{base}.000005')
    assert result.microsecond == 5
    result = Timestamp(base.value + Timedelta('5ns').value)
    assert result == Timestamp(f'{base}.000000005')
    assert result.nanosecond == 5
    assert result.microsecond == 0
    result = Timestamp(base.value + Timedelta('6ms 5us').value)
    assert result == Timestamp(f'{base}.006005')
    assert result.microsecond == 5 + 6 * 1000
    result = Timestamp(base.value + Timedelta('200ms 5us').value)
    assert result == Timestamp(f'{base}.200005')
    assert result.microsecond == 5 + 200 * 1000