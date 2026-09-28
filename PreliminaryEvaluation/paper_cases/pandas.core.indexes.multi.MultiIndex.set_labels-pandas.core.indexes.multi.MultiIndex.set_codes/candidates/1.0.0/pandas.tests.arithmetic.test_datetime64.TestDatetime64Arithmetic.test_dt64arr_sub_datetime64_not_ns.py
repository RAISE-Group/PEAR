def test_dt64arr_sub_datetime64_not_ns(self, box_with_array):
    dt64 = np.datetime64('2013-01-01')
    assert dt64.dtype == 'datetime64[D]'
    dti = pd.date_range('20130101', periods=3)
    dtarr = tm.box_expected(dti, box_with_array)
    expected = pd.TimedeltaIndex(['0 Days', '1 Day', '2 Days'])
    expected = tm.box_expected(expected, box_with_array)
    result = dtarr - dt64
    tm.assert_equal(result, expected)
    result = dt64 - dtarr
    tm.assert_equal(result, -expected)