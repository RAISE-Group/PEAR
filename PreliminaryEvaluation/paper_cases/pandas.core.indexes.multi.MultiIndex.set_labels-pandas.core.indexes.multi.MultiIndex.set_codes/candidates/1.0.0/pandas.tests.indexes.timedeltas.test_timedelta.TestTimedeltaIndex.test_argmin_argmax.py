def test_argmin_argmax(self):
    idx = TimedeltaIndex(['1 day 00:00:05', '1 day 00:00:01', '1 day 00:00:02'])
    assert idx.argmin() == 1
    assert idx.argmax() == 0