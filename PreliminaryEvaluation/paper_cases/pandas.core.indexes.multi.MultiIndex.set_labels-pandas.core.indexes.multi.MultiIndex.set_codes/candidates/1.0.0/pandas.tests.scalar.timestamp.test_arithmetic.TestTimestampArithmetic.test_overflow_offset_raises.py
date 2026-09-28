def test_overflow_offset_raises(self):
    stamp = Timestamp('2017-01-13 00:00:00', freq='D')
    offset_overflow = 20169940 * offsets.Day(1)
    msg = 'the add operation between \\<-?\\d+ \\* Days\\> and \\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2} will overflow'
    with pytest.raises(OverflowError, match=msg):
        stamp + offset_overflow
    with pytest.raises(OverflowError, match=msg):
        offset_overflow + stamp
    with pytest.raises(OverflowError, match=msg):
        stamp - offset_overflow
    stamp = Timestamp('2000/1/1')
    offset_overflow = to_offset('D') * 100 ** 25
    with pytest.raises(OverflowError, match=msg):
        stamp + offset_overflow
    with pytest.raises(OverflowError, match=msg):
        offset_overflow + stamp
    with pytest.raises(OverflowError, match=msg):
        stamp - offset_overflow