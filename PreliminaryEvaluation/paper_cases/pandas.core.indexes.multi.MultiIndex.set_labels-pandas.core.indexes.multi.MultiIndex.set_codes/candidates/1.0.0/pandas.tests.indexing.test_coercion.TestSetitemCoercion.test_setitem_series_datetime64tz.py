@pytest.mark.parametrize('val,exp_dtype', [(pd.Timestamp('2012-01-01', tz='US/Eastern'), 'datetime64[ns, US/Eastern]'), (pd.Timestamp('2012-01-01', tz='US/Pacific'), np.object), (pd.Timestamp('2012-01-01'), np.object), (1, np.object)])
def test_setitem_series_datetime64tz(self, val, exp_dtype):
    tz = 'US/Eastern'
    obj = pd.Series([pd.Timestamp('2011-01-01', tz=tz), pd.Timestamp('2011-01-02', tz=tz), pd.Timestamp('2011-01-03', tz=tz), pd.Timestamp('2011-01-04', tz=tz)])
    assert obj.dtype == 'datetime64[ns, US/Eastern]'
    exp = pd.Series([pd.Timestamp('2011-01-01', tz=tz), val, pd.Timestamp('2011-01-03', tz=tz), pd.Timestamp('2011-01-04', tz=tz)])
    self._assert_setitem_series_conversion(obj, val, exp, exp_dtype)