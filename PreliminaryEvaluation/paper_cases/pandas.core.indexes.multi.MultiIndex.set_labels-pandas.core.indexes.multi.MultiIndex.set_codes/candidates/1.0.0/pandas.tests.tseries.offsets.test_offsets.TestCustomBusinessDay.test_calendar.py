@pytest.mark.filterwarnings('ignore:Non:pandas.errors.PerformanceWarning')
def test_calendar(self):
    calendar = USFederalHolidayCalendar()
    dt = datetime(2014, 1, 17)
    assert_offset_equal(CDay(calendar=calendar), dt, datetime(2014, 1, 21))