@pytest.mark.parametrize('fill_val,fill_dtype', [(pd.Timestamp('2012-01-01', tz='US/Eastern'), 'datetime64[ns, US/Eastern]'), (pd.Timestamp('2012-01-01'), np.object), (pd.Timestamp('2012-01-01', tz='Asia/Tokyo'), np.object), (1, np.object), ('x', np.object)])
def test_fillna_datetime64tz(self, index_or_series, fill_val, fill_dtype):
    klass = index_or_series
    tz = 'US/Eastern'
    obj = klass([pd.Timestamp('2011-01-01', tz=tz), pd.NaT, pd.Timestamp('2011-01-03', tz=tz), pd.Timestamp('2011-01-04', tz=tz)])
    assert obj.dtype == 'datetime64[ns, US/Eastern]'
    exp = klass([pd.Timestamp('2011-01-01', tz=tz), fill_val, pd.Timestamp('2011-01-03', tz=tz), pd.Timestamp('2011-01-04', tz=tz)])
    self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)