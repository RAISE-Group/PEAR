def test_tdi_add_dt64_array(self, box_with_array):
    dti = pd.date_range('2016-01-01', periods=3)
    tdi = dti - dti.shift(1)
    dtarr = dti.values
    expected = pd.DatetimeIndex(dtarr) + tdi
    tdi = tm.box_expected(tdi, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    result = tdi + dtarr
    tm.assert_equal(result, expected)
    result = dtarr + tdi
    tm.assert_equal(result, expected)