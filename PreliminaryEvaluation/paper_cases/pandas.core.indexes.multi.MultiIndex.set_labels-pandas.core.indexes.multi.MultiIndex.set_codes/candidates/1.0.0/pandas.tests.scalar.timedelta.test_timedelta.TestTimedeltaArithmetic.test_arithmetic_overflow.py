def test_arithmetic_overflow(self):
    with pytest.raises(OverflowError):
        Timestamp('1700-01-01') + Timedelta(13 * 19999, unit='D')
    with pytest.raises(OverflowError):
        Timestamp('1700-01-01') + timedelta(days=13 * 19999)