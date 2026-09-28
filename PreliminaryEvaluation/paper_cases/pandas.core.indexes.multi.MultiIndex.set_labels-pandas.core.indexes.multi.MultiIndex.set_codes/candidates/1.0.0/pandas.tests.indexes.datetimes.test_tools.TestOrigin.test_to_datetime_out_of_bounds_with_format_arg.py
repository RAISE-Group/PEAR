@pytest.mark.parametrize('format', [None, '%Y-%m-%d %H:%M:%S'])
def test_to_datetime_out_of_bounds_with_format_arg(self, format):
    msg = 'Out of bounds nanosecond timestamp'
    with pytest.raises(OutOfBoundsDatetime, match=msg):
        to_datetime('2417-10-27 00:00:00', format=format)