@pytest.mark.parametrize('tz', ['UTC', 'US/Eastern'])
@pytest.mark.parametrize('constructor', ['M8', 'datetime64'])
def test_parser(self, tz, constructor):
    dtz_str = f'{constructor}[ns, {tz}]'
    result = DatetimeTZDtype.construct_from_string(dtz_str)
    expected = DatetimeTZDtype('ns', tz)
    assert result == expected