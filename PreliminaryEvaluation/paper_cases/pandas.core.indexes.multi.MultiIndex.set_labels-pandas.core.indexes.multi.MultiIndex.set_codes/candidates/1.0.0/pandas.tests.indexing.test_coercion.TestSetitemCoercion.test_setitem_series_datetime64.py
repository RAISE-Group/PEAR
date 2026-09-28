@pytest.mark.parametrize('val,exp_dtype', [(pd.Timestamp('2012-01-01'), 'datetime64[ns]'), (1, np.object), ('x', np.object)])
def test_setitem_series_datetime64(self, val, exp_dtype):
    obj = pd.Series([pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02'), pd.Timestamp('2011-01-03'), pd.Timestamp('2011-01-04')])
    assert obj.dtype == 'datetime64[ns]'
    exp = pd.Series([pd.Timestamp('2011-01-01'), val, pd.Timestamp('2011-01-03'), pd.Timestamp('2011-01-04')])
    self._assert_setitem_series_conversion(obj, val, exp, exp_dtype)