def test_combine_first_dt_tz_values(self, tz_naive_fixture):
    ser1 = pd.Series(pd.DatetimeIndex(['20150101', '20150102', '20150103'], tz=tz_naive_fixture), name='ser1')
    ser2 = pd.Series(pd.DatetimeIndex(['20160514', '20160515', '20160516'], tz=tz_naive_fixture), index=[2, 3, 4], name='ser2')
    result = ser1.combine_first(ser2)
    exp_vals = pd.DatetimeIndex(['20150101', '20150102', '20150103', '20160515', '20160516'], tz=tz_naive_fixture)
    exp = pd.Series(exp_vals, name='ser1')
    tm.assert_series_equal(exp, result)