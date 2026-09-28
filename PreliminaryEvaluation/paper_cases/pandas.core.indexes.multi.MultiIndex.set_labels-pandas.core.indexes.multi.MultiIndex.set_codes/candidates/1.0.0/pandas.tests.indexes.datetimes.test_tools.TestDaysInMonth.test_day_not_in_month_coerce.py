@pytest.mark.parametrize('cache', [True, False])
def test_day_not_in_month_coerce(self, cache):
    assert isna(to_datetime('2015-02-29', errors='coerce', cache=cache))
    assert isna(to_datetime('2015-02-29', format='%Y-%m-%d', errors='coerce', cache=cache))
    assert isna(to_datetime('2015-02-32', format='%Y-%m-%d', errors='coerce', cache=cache))
    assert isna(to_datetime('2015-04-31', format='%Y-%m-%d', errors='coerce', cache=cache))