@pytest.mark.parametrize('tz', ['US/Pacific', 'US/Eastern', 'Asia/Tokyo'])
def test_constructor_with_non_normalized_pytz(self, tz):
    non_norm_tz = Timestamp('2010', tz=tz).tz
    result = DatetimeIndex(['2010'], tz=non_norm_tz)
    assert pytz.timezone(tz) is result.tz