@pytest.mark.parametrize('offset', ['+0300', '+0200'])
def test_construct_timestamp_near_dst(self, offset):
    expected = Timestamp('2016-10-30 03:00:00{}'.format(offset), tz='Europe/Helsinki')
    result = Timestamp(expected).tz_convert('Europe/Helsinki')
    assert result == expected