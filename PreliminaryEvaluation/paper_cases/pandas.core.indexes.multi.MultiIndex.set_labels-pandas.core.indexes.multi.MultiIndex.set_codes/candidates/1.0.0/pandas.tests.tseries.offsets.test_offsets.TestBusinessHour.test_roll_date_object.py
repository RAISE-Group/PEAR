def test_roll_date_object(self):
    offset = BusinessHour()
    dt = datetime(2014, 7, 6, 15, 0)
    result = offset.rollback(dt)
    assert result == datetime(2014, 7, 4, 17)
    result = offset.rollforward(dt)
    assert result == datetime(2014, 7, 7, 9)