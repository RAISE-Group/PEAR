def test_isnumeric(self):
    values = ['A', '3', '¼', '★', '፸', '３', 'four']
    s = Series(values)
    numeric_e = [False, True, True, False, True, True, False]
    decimal_e = [False, True, False, False, False, True, False]
    tm.assert_series_equal(s.str.isnumeric(), Series(numeric_e))
    tm.assert_series_equal(s.str.isdecimal(), Series(decimal_e))
    unicodes = ['A', '3', '¼', '★', '፸', '３', 'four']
    assert s.str.isnumeric().tolist() == [v.isnumeric() for v in unicodes]
    assert s.str.isdecimal().tolist() == [v.isdecimal() for v in unicodes]
    values = ['A', np.nan, '¼', '★', np.nan, '３', 'four']
    s = Series(values)
    numeric_e = [False, np.nan, True, False, np.nan, True, False]
    decimal_e = [False, np.nan, False, False, np.nan, True, False]
    tm.assert_series_equal(s.str.isnumeric(), Series(numeric_e))
    tm.assert_series_equal(s.str.isdecimal(), Series(decimal_e))