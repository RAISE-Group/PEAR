def test_constructor_errors(self):
    from datetime import time as dt_time
    with pytest.raises(ValueError):
        CustomBusinessHour(start=dt_time(11, 0, 5))
    with pytest.raises(ValueError):
        CustomBusinessHour(start='AAA')
    with pytest.raises(ValueError):
        CustomBusinessHour(start='14:00:05')