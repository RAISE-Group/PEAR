@pytest.mark.parametrize('fill_val,exp_dtype', [(pd.Timestamp('2012-01-01'), 'datetime64[ns]'), (pd.Timestamp('2012-01-01', tz='US/Eastern'), np.object)], ids=['datetime64', 'datetime64tz'])
def test_where_series_datetime64(self, fill_val, exp_dtype):
    obj = pd.Series([pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02'), pd.Timestamp('2011-01-03'), pd.Timestamp('2011-01-04')])
    assert obj.dtype == 'datetime64[ns]'
    cond = pd.Series([True, False, True, False])
    exp = pd.Series([pd.Timestamp('2011-01-01'), fill_val, pd.Timestamp('2011-01-03'), fill_val])
    self._assert_where_conversion(obj, cond, fill_val, exp, exp_dtype)
    values = pd.Series(pd.date_range(fill_val, periods=4))
    if fill_val.tz:
        exp = pd.Series([pd.Timestamp('2011-01-01'), pd.Timestamp('2012-01-02 00:00', tz='US/Eastern'), pd.Timestamp('2011-01-03'), pd.Timestamp('2012-01-04 00:00', tz='US/Eastern')])
        self._assert_where_conversion(obj, cond, values, exp, exp_dtype)
    exp = pd.Series([pd.Timestamp('2011-01-01'), values[1], pd.Timestamp('2011-01-03'), values[3]])
    self._assert_where_conversion(obj, cond, values, exp, exp_dtype)