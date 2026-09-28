@pytest.mark.parametrize('offset', ['+0', '-1foo', 'UTCbar', ':10', '+01:000:01', ''])
def test_to_datetime_parse_timezone_malformed(self, offset):
    fmt = '%Y-%m-%d %H:%M:%S %z'
    date = '2010-01-01 12:00:00 ' + offset
    with pytest.raises(ValueError):
        pd.to_datetime([date], format=fmt)