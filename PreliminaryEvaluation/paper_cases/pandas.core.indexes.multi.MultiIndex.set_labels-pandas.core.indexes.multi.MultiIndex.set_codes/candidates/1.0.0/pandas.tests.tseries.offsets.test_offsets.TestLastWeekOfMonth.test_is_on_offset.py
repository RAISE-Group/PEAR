@pytest.mark.parametrize('case', on_offset_cases)
def test_is_on_offset(self, case):
    weekday, dt, expected = case
    offset = LastWeekOfMonth(weekday=weekday)
    assert offset.is_on_offset(dt) == expected