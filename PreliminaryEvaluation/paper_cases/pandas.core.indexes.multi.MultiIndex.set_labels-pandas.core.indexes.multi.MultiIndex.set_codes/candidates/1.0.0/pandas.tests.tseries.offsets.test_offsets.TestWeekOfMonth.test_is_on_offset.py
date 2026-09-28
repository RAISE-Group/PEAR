@pytest.mark.parametrize('case', on_offset_cases)
def test_is_on_offset(self, case):
    week, weekday, dt, expected = case
    offset = WeekOfMonth(week=week, weekday=weekday)
    assert offset.is_on_offset(dt) == expected