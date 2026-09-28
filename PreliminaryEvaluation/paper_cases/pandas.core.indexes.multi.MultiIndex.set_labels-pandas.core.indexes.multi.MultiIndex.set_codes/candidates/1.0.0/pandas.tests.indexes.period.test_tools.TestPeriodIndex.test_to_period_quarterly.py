@pytest.mark.parametrize('month', MONTHS)
def test_to_period_quarterly(self, month):
    freq = 'Q-{month}'.format(month=month)
    rng = period_range('1989Q3', '1991Q3', freq=freq)
    stamps = rng.to_timestamp()
    result = stamps.to_period(freq)
    tm.assert_index_equal(rng, result)