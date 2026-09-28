def test_tda_add_sub_index(self):
    tdi = TimedeltaIndex(['1 days', pd.NaT, '2 days'])
    tda = tdi.array
    dti = pd.date_range('1999-12-31', periods=3, freq='D')
    result = tda + dti
    expected = tdi + dti
    tm.assert_index_equal(result, expected)
    result = tda + tdi
    expected = tdi + tdi
    tm.assert_index_equal(result, expected)
    result = tda - tdi
    expected = tdi - tdi
    tm.assert_index_equal(result, expected)