def test_tz_setter_raises(self):
    arr = DatetimeArray._from_sequence(['2000'], tz='US/Central')
    with pytest.raises(AttributeError, match='tz_localize'):
        arr.tz = 'UTC'