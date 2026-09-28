@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_dti_take_dont_lose_meta(self, tzstr):
    rng = date_range('1/1/2000', periods=20, tz=tzstr)
    result = rng.take(range(5))
    assert result.tz == rng.tz
    assert result.freq == rng.freq