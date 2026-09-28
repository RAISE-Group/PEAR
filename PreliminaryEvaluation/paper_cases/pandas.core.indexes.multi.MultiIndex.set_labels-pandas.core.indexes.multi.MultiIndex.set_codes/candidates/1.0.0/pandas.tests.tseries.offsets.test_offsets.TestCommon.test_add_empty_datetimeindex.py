def test_add_empty_datetimeindex(self, offset_types, tz_naive_fixture):
    offset_s = self._get_offset(offset_types)
    dti = DatetimeIndex([], tz=tz_naive_fixture)
    warn = None
    if isinstance(offset_s, (Easter, WeekOfMonth, LastWeekOfMonth, CustomBusinessDay, BusinessHour, CustomBusinessHour, CustomBusinessMonthBegin, CustomBusinessMonthEnd, FY5253, FY5253Quarter)):
        warn = PerformanceWarning
    with tm.assert_produces_warning(warn):
        result = dti + offset_s
    tm.assert_index_equal(result, dti)
    with tm.assert_produces_warning(warn):
        result = offset_s + dti
    tm.assert_index_equal(result, dti)
    dta = dti._data
    with tm.assert_produces_warning(warn):
        result = dta + offset_s
    tm.assert_equal(result, dta)
    with tm.assert_produces_warning(warn):
        result = offset_s + dta
    tm.assert_equal(result, dta)