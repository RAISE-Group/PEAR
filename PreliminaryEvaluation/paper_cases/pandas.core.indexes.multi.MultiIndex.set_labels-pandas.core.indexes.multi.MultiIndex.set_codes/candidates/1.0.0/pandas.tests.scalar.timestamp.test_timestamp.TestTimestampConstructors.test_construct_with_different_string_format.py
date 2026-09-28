@pytest.mark.parametrize('arg', ['2013/01/01 00:00:00+09:00', '2013-01-01 00:00:00+09:00'])
def test_construct_with_different_string_format(self, arg):
    result = Timestamp(arg)
    expected = Timestamp(datetime(2013, 1, 1), tz=pytz.FixedOffset(540))
    assert result == expected