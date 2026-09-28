def test_td64arr_sub_offset_array(self, box_with_array):
    tdi = TimedeltaIndex(['1 days 00:00:00', '3 days 04:00:00'])
    other = np.array([pd.offsets.Hour(n=1), pd.offsets.Minute(n=-2)])
    expected = TimedeltaIndex([tdi[n] - other[n] for n in range(len(tdi))], freq='infer')
    tdi = tm.box_expected(tdi, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    warn = None if box_with_array is pd.DataFrame else PerformanceWarning
    with tm.assert_produces_warning(warn):
        res = tdi - other
    tm.assert_equal(res, expected)