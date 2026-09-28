def test_insert_index_timedelta64(self):
    obj = pd.TimedeltaIndex(['1 day', '2 day', '3 day', '4 day'])
    assert obj.dtype == 'timedelta64[ns]'
    exp = pd.TimedeltaIndex(['1 day', '10 day', '2 day', '3 day', '4 day'])
    self._assert_insert_conversion(obj, pd.Timedelta('10 day'), exp, 'timedelta64[ns]')
    msg = 'cannot insert TimedeltaIndex with incompatible label'
    with pytest.raises(TypeError, match=msg):
        obj.insert(1, pd.Timestamp('2012-01-01'))
    msg = 'cannot insert TimedeltaIndex with incompatible label'
    with pytest.raises(TypeError, match=msg):
        obj.insert(1, 1)