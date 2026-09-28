@pytest.mark.parametrize('val,exp_dtype', [(pd.Timedelta('12 day'), 'timedelta64[ns]'), (1, np.object), ('x', np.object)])
def test_setitem_series_timedelta64(self, val, exp_dtype):
    obj = pd.Series([pd.Timedelta('1 day'), pd.Timedelta('2 day'), pd.Timedelta('3 day'), pd.Timedelta('4 day')])
    assert obj.dtype == 'timedelta64[ns]'
    exp = pd.Series([pd.Timedelta('1 day'), val, pd.Timedelta('3 day'), pd.Timedelta('4 day')])
    self._assert_setitem_series_conversion(obj, val, exp, exp_dtype)