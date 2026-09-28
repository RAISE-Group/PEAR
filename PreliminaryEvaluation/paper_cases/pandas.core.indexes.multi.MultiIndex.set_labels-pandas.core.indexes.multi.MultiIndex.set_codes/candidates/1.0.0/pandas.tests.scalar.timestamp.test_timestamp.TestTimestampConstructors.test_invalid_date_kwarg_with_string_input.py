@pytest.mark.parametrize('arg', ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond', 'nanosecond'])
def test_invalid_date_kwarg_with_string_input(self, arg):
    kwarg = {arg: 1}
    with pytest.raises(ValueError):
        Timestamp('2010-10-10 12:59:59.999999999', **kwarg)