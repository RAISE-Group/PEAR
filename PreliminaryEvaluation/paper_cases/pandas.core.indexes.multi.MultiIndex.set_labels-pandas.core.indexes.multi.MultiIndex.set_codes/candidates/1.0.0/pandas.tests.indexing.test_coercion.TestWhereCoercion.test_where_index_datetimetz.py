@pytest.mark.xfail(reason='GH 22839: do not ignore timezone, must be object')
def test_where_index_datetimetz(self):
    fill_val = pd.Timestamp('2012-01-01', tz='US/Eastern')
    exp_dtype = np.object
    obj = pd.Index([pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02'), pd.Timestamp('2011-01-03'), pd.Timestamp('2011-01-04')])
    assert obj.dtype == 'datetime64[ns]'
    cond = pd.Index([True, False, True, False])
    msg = 'Index\\(\\.\\.\\.\\) must be called with a collection of some kind'
    with pytest.raises(TypeError, match=msg):
        obj.where(cond, fill_val)
    values = pd.Index(pd.date_range(fill_val, periods=4))
    exp = pd.Index([pd.Timestamp('2011-01-01'), pd.Timestamp('2012-01-02', tz='US/Eastern'), pd.Timestamp('2011-01-03'), pd.Timestamp('2012-01-04', tz='US/Eastern')], dtype=exp_dtype)
    self._assert_where_conversion(obj, cond, values, exp, exp_dtype)