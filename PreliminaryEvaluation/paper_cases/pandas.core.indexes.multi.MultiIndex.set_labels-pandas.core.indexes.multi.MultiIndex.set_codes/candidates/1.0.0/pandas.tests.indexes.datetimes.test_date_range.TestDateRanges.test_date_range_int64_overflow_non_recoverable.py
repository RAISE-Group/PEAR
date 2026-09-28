def test_date_range_int64_overflow_non_recoverable(self):
    msg = 'Cannot generate range with'
    with pytest.raises(OutOfBoundsDatetime, match=msg):
        date_range(start='1970-02-01', periods=106752 * 24, freq='H')
    with pytest.raises(OutOfBoundsDatetime, match=msg):
        date_range(end='1969-11-14', periods=106752 * 24, freq='H')