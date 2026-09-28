def test_subtype_datetimelike(self):
    dtype = IntervalDtype('timedelta64[ns]')
    msg = 'Cannot convert .* to .*; subtypes are incompatible'
    index = interval_range(Timestamp('2018-01-01'), periods=10)
    with pytest.raises(TypeError, match=msg):
        index.astype(dtype)
    index = interval_range(Timestamp('2018-01-01', tz='CET'), periods=10)
    with pytest.raises(TypeError, match=msg):
        index.astype(dtype)
    dtype = IntervalDtype('datetime64[ns]')
    index = interval_range(Timedelta('0 days'), periods=10)
    with pytest.raises(TypeError, match=msg):
        index.astype(dtype)