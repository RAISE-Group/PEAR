def test_is_anchored(self):
    assert makeFY5253LastOfMonthQuarter(startingMonth=1, weekday=WeekDay.SAT, qtr_with_extra_week=4).is_anchored()
    assert makeFY5253LastOfMonthQuarter(weekday=WeekDay.SAT, startingMonth=3, qtr_with_extra_week=4).is_anchored()
    assert not makeFY5253LastOfMonthQuarter(2, startingMonth=1, weekday=WeekDay.SAT, qtr_with_extra_week=4).is_anchored()