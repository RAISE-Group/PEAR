def test_catch_infinite_loop(self):
    offset = offsets.DateOffset(minute=5)
    msg = 'Offset <DateOffset: minute=5> did not increment date'
    with pytest.raises(ValueError, match=msg):
        date_range(datetime(2011, 11, 11), datetime(2011, 11, 12), freq=offset)