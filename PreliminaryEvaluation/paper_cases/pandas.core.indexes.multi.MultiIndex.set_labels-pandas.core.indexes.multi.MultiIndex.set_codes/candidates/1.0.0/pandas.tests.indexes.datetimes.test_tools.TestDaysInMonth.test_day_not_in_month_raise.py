@pytest.mark.parametrize('cache', [True, False])
def test_day_not_in_month_raise(self, cache):
    msg = 'day is out of range for month'
    with pytest.raises(ValueError, match=msg):
        to_datetime('2015-02-29', errors='raise', cache=cache)
    msg = "time data 2015-02-29 doesn't match format specified"
    with pytest.raises(ValueError, match=msg):
        to_datetime('2015-02-29', errors='raise', format='%Y-%m-%d', cache=cache)
    msg = "time data 2015-02-32 doesn't match format specified"
    with pytest.raises(ValueError, match=msg):
        to_datetime('2015-02-32', errors='raise', format='%Y-%m-%d', cache=cache)
    msg = "time data 2015-04-31 doesn't match format specified"
    with pytest.raises(ValueError, match=msg):
        to_datetime('2015-04-31', errors='raise', format='%Y-%m-%d', cache=cache)