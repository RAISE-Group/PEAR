def test_to_datetime_fixed_offset(self):
    dates = [datetime(2000, 1, 1, tzinfo=fixed_off), datetime(2000, 1, 2, tzinfo=fixed_off), datetime(2000, 1, 3, tzinfo=fixed_off)]
    result = to_datetime(dates)
    assert result.tz == fixed_off