def test_dt64arr_add_sub_offset_ndarray(self, tz_naive_fixture, box_with_array):
    tz = tz_naive_fixture
    dti = pd.date_range('2017-01-01', periods=2, tz=tz)
    dtarr = tm.box_expected(dti, box_with_array)
    other = np.array([pd.offsets.MonthEnd(), pd.offsets.Day(n=2)])
    warn = None if box_with_array is pd.DataFrame else PerformanceWarning
    with tm.assert_produces_warning(warn):
        res = dtarr + other
    expected = DatetimeIndex([dti[n] + other[n] for n in range(len(dti))], name=dti.name, freq='infer')
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(res, expected)
    with tm.assert_produces_warning(warn):
        res2 = other + dtarr
    tm.assert_equal(res2, expected)
    with tm.assert_produces_warning(warn):
        res = dtarr - other
    expected = DatetimeIndex([dti[n] - other[n] for n in range(len(dti))], name=dti.name, freq='infer')
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(res, expected)