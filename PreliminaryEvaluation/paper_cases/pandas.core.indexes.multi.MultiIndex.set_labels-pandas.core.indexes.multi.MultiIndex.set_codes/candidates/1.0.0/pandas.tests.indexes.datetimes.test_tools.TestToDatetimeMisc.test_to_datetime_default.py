@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_default(self, cache):
    rs = to_datetime('2001', cache=cache)
    xp = datetime(2001, 1, 1)
    assert rs == xp