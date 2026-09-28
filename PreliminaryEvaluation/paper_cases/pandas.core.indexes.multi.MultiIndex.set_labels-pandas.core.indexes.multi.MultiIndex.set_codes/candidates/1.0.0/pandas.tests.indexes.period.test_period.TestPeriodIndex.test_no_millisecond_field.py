def test_no_millisecond_field(self):
    msg = "type object 'DatetimeIndex' has no attribute 'millisecond'"
    with pytest.raises(AttributeError, match=msg):
        DatetimeIndex.millisecond
    msg = "'DatetimeIndex' object has no attribute 'millisecond'"
    with pytest.raises(AttributeError, match=msg):
        DatetimeIndex([]).millisecond