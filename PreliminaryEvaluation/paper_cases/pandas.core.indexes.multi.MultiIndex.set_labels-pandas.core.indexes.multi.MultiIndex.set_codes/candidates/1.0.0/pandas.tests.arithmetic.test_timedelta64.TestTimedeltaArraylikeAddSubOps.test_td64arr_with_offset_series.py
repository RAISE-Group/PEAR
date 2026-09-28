@pytest.mark.parametrize('names', [(None, None, None), ('foo', 'bar', None), ('foo', 'foo', 'foo')])
def test_td64arr_with_offset_series(self, names, box_df_fail):
    box = box_df_fail
    box2 = Series if box in [pd.Index, tm.to_array] else box
    exname = names[2] if box is not tm.to_array else names[1]
    tdi = TimedeltaIndex(['1 days 00:00:00', '3 days 04:00:00'], name=names[0])
    other = Series([pd.offsets.Hour(n=1), pd.offsets.Minute(n=-2)], name=names[1])
    expected_add = Series([tdi[n] + other[n] for n in range(len(tdi))], name=exname)
    tdi = tm.box_expected(tdi, box)
    expected_add = tm.box_expected(expected_add, box2)
    with tm.assert_produces_warning(PerformanceWarning):
        res = tdi + other
    tm.assert_equal(res, expected_add)
    with tm.assert_produces_warning(PerformanceWarning):
        res2 = other + tdi
    tm.assert_equal(res2, expected_add)
    expected_sub = Series([tdi[n] - other[n] for n in range(len(tdi))], name=exname)
    expected_sub = tm.box_expected(expected_sub, box2)
    with tm.assert_produces_warning(PerformanceWarning):
        res3 = tdi - other
    tm.assert_equal(res3, expected_sub)