def test_repr(self):
    assert repr(WeekOfMonth(weekday=1, week=2)) == '<WeekOfMonth: week=2, weekday=1>'