@pytest.mark.filterwarnings('ignore:Non:pandas.errors.PerformanceWarning')
def test_datetimeindex(self):
    from pandas.tseries.holiday import USFederalHolidayCalendar
    hcal = USFederalHolidayCalendar()
    freq = CBMonthEnd(calendar=hcal)
    assert date_range(start='20120101', end='20130101', freq=freq).tolist()[0] == datetime(2012, 1, 31)