def test_constructor_invalid_tz(self):
    with pytest.raises(TypeError, match='must be a datetime.tzinfo'):
        Timestamp('2017-10-22', tzinfo='US/Eastern')
    with pytest.raises(ValueError, match='at most one of'):
        Timestamp('2017-10-22', tzinfo=utc, tz='UTC')
    with pytest.raises(ValueError, match='Invalid frequency:'):
        Timestamp('2012-01-01', 'US/Pacific')