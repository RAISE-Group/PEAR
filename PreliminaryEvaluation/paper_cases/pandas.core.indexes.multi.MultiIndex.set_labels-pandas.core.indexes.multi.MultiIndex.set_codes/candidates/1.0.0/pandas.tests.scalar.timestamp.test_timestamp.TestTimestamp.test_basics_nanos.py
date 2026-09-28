def test_basics_nanos(self):
    val = np.int64(946684800000000000).view('M8[ns]')
    stamp = Timestamp(val.view('i8') + 500)
    assert stamp.year == 2000
    assert stamp.month == 1
    assert stamp.microsecond == 0
    assert stamp.nanosecond == 500
    val = np.iinfo(np.int64).min + 80000000000000
    stamp = Timestamp(val)
    assert stamp.year == 1677
    assert stamp.month == 9
    assert stamp.day == 21
    assert stamp.microsecond == 145224
    assert stamp.nanosecond == 192