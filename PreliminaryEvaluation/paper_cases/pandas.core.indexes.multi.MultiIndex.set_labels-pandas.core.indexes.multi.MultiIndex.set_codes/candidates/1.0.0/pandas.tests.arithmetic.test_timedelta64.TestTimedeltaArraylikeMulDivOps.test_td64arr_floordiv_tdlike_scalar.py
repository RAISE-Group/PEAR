def test_td64arr_floordiv_tdlike_scalar(self, two_hours, box_with_array):
    tdi = timedelta_range('1 days', '10 days', name='foo')
    expected = pd.Int64Index((np.arange(10) + 1) * 12, name='foo')
    tdi = tm.box_expected(tdi, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    result = tdi // two_hours
    tm.assert_equal(result, expected)