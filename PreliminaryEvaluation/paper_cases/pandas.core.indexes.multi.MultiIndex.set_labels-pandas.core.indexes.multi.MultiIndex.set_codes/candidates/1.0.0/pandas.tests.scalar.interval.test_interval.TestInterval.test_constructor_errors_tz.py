@pytest.mark.parametrize('tz_left, tz_right', [(None, 'UTC'), ('UTC', None), ('UTC', 'US/Eastern')])
def test_constructor_errors_tz(self, tz_left, tz_right):
    left = Timestamp('2017-01-01', tz=tz_left)
    right = Timestamp('2017-01-02', tz=tz_right)
    error = TypeError if com.any_none(tz_left, tz_right) else ValueError
    with pytest.raises(error):
        Interval(left, right)