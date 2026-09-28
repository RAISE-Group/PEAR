@pytest.mark.parametrize('cache', [True, False])
def test_day_not_in_month_ignore(self, cache):
    assert to_datetime('2015-02-29', errors='ignore', cache=cache) == '2015-02-29'
    assert to_datetime('2015-02-29', errors='ignore', format='%Y-%m-%d', cache=cache) == '2015-02-29'
    assert to_datetime('2015-02-32', errors='ignore', format='%Y-%m-%d', cache=cache) == '2015-02-32'
    assert to_datetime('2015-04-31', errors='ignore', format='%Y-%m-%d', cache=cache) == '2015-04-31'