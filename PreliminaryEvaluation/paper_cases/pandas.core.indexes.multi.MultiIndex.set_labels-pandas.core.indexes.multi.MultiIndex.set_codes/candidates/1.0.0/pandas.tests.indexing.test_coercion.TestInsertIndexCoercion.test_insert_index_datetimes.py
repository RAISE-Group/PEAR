@pytest.mark.parametrize('fill_val,exp_dtype', [(pd.Timestamp('2012-01-01'), 'datetime64[ns]'), (pd.Timestamp('2012-01-01', tz='US/Eastern'), 'datetime64[ns, US/Eastern]')], ids=['datetime64', 'datetime64tz'])
def test_insert_index_datetimes(self, fill_val, exp_dtype):
    obj = pd.DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04'], tz=fill_val.tz)
    assert obj.dtype == exp_dtype
    exp = pd.DatetimeIndex(['2011-01-01', fill_val.date(), '2011-01-02', '2011-01-03', '2011-01-04'], tz=fill_val.tz)
    self._assert_insert_conversion(obj, fill_val, exp, exp_dtype)
    if fill_val.tz:
        msg = 'Cannot compare tz-naive and tz-aware'
        with pytest.raises(TypeError, match=msg):
            obj.insert(1, pd.Timestamp('2012-01-01'))
        msg = "Timezones don't match"
        with pytest.raises(ValueError, match=msg):
            obj.insert(1, pd.Timestamp('2012-01-01', tz='Asia/Tokyo'))
    else:
        msg = 'Cannot compare tz-naive and tz-aware'
        with pytest.raises(TypeError, match=msg):
            obj.insert(1, pd.Timestamp('2012-01-01', tz='Asia/Tokyo'))
    msg = 'cannot insert DatetimeIndex with incompatible label'
    with pytest.raises(TypeError, match=msg):
        obj.insert(1, 1)
    pytest.xfail('ToDo: must coerce to object')