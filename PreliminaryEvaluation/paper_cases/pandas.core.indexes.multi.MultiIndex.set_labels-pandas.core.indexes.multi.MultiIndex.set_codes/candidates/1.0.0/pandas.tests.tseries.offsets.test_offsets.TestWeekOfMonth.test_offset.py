def test_offset(self):
    date1 = datetime(2011, 1, 4)
    date2 = datetime(2011, 1, 11)
    date3 = datetime(2011, 1, 18)
    date4 = datetime(2011, 1, 25)
    test_cases = [(-2, 2, 1, date1, datetime(2010, 11, 16)), (-2, 2, 1, date2, datetime(2010, 11, 16)), (-2, 2, 1, date3, datetime(2010, 11, 16)), (-2, 2, 1, date4, datetime(2010, 12, 21)), (-1, 2, 1, date1, datetime(2010, 12, 21)), (-1, 2, 1, date2, datetime(2010, 12, 21)), (-1, 2, 1, date3, datetime(2010, 12, 21)), (-1, 2, 1, date4, datetime(2011, 1, 18)), (0, 0, 1, date1, datetime(2011, 1, 4)), (0, 0, 1, date2, datetime(2011, 2, 1)), (0, 0, 1, date3, datetime(2011, 2, 1)), (0, 0, 1, date4, datetime(2011, 2, 1)), (0, 1, 1, date1, datetime(2011, 1, 11)), (0, 1, 1, date2, datetime(2011, 1, 11)), (0, 1, 1, date3, datetime(2011, 2, 8)), (0, 1, 1, date4, datetime(2011, 2, 8)), (0, 0, 1, date1, datetime(2011, 1, 4)), (0, 1, 1, date2, datetime(2011, 1, 11)), (0, 2, 1, date3, datetime(2011, 1, 18)), (0, 3, 1, date4, datetime(2011, 1, 25)), (1, 0, 0, date1, datetime(2011, 2, 7)), (1, 0, 0, date2, datetime(2011, 2, 7)), (1, 0, 0, date3, datetime(2011, 2, 7)), (1, 0, 0, date4, datetime(2011, 2, 7)), (1, 0, 1, date1, datetime(2011, 2, 1)), (1, 0, 1, date2, datetime(2011, 2, 1)), (1, 0, 1, date3, datetime(2011, 2, 1)), (1, 0, 1, date4, datetime(2011, 2, 1)), (1, 0, 2, date1, datetime(2011, 1, 5)), (1, 0, 2, date2, datetime(2011, 2, 2)), (1, 0, 2, date3, datetime(2011, 2, 2)), (1, 0, 2, date4, datetime(2011, 2, 2)), (1, 2, 1, date1, datetime(2011, 1, 18)), (1, 2, 1, date2, datetime(2011, 1, 18)), (1, 2, 1, date3, datetime(2011, 2, 15)), (1, 2, 1, date4, datetime(2011, 2, 15)), (2, 2, 1, date1, datetime(2011, 2, 15)), (2, 2, 1, date2, datetime(2011, 2, 15)), (2, 2, 1, date3, datetime(2011, 3, 15)), (2, 2, 1, date4, datetime(2011, 3, 15))]
    for n, week, weekday, dt, expected in test_cases:
        offset = WeekOfMonth(n, week=week, weekday=weekday)
        assert_offset_equal(offset, dt, expected)
    result = datetime(2011, 2, 1) - WeekOfMonth(week=1, weekday=2)
    assert result == datetime(2011, 1, 12)
    result = datetime(2011, 2, 3) - WeekOfMonth(week=0, weekday=2)
    assert result == datetime(2011, 2, 2)