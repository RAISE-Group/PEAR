def test_dti_to_pydatetime_fizedtz(self):
    dates = np.array([datetime(2000, 1, 1, tzinfo=fixed_off), datetime(2000, 1, 2, tzinfo=fixed_off), datetime(2000, 1, 3, tzinfo=fixed_off)])
    dti = DatetimeIndex(dates)
    result = dti.to_pydatetime()
    tm.assert_numpy_array_equal(dates, result)
    result = dti._mpl_repr()
    tm.assert_numpy_array_equal(dates, result)