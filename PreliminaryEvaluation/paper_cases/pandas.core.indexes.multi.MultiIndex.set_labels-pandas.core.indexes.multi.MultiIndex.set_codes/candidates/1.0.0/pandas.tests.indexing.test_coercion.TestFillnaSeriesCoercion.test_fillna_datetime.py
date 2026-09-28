@pytest.mark.parametrize('fill_val,fill_dtype', [(pd.Timestamp('2012-01-01'), 'datetime64[ns]'), (pd.Timestamp('2012-01-01', tz='US/Eastern'), np.object), (1, np.object), ('x', np.object)], ids=['datetime64', 'datetime64tz', 'object', 'object'])
def test_fillna_datetime(self, index_or_series, fill_val, fill_dtype):
    klass = index_or_series
    obj = klass([pd.Timestamp('2011-01-01'), pd.NaT, pd.Timestamp('2011-01-03'), pd.Timestamp('2011-01-04')])
    assert obj.dtype == 'datetime64[ns]'
    exp = klass([pd.Timestamp('2011-01-01'), fill_val, pd.Timestamp('2011-01-03'), pd.Timestamp('2011-01-04')])
    self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)