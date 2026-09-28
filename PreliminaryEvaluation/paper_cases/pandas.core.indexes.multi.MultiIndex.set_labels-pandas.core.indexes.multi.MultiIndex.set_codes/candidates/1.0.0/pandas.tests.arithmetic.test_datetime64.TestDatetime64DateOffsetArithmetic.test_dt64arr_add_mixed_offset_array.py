def test_dt64arr_add_mixed_offset_array(self, box_with_array):
    s = DatetimeIndex([Timestamp('2000-1-1'), Timestamp('2000-2-1')])
    s = tm.box_expected(s, box_with_array)
    warn = None if box_with_array is pd.DataFrame else PerformanceWarning
    with tm.assert_produces_warning(warn):
        other = pd.Index([pd.offsets.DateOffset(years=1), pd.offsets.MonthEnd()])
        other = tm.box_expected(other, box_with_array)
        result = s + other
        exp = DatetimeIndex([Timestamp('2001-1-1'), Timestamp('2000-2-29')])
        exp = tm.box_expected(exp, box_with_array)
        tm.assert_equal(result, exp)
        other = pd.Index([pd.offsets.DateOffset(years=1), pd.offsets.DateOffset(years=1)])
        other = tm.box_expected(other, box_with_array)
        result = s + other
        exp = DatetimeIndex([Timestamp('2001-1-1'), Timestamp('2001-2-1')])
        exp = tm.box_expected(exp, box_with_array)
        tm.assert_equal(result, exp)