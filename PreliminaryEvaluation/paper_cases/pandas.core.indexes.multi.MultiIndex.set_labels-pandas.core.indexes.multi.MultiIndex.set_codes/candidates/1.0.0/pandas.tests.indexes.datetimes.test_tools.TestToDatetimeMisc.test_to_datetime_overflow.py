def test_to_datetime_overflow(self):
    with pytest.raises(OverflowError):
        date_range(start='1/1/1700', freq='B', periods=100000)