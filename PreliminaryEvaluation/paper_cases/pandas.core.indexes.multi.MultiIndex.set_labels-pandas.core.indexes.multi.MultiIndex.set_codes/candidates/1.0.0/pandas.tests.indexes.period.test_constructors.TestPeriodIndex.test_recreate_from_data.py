@pytest.mark.parametrize('freq', ['M', 'Q', 'A', 'D', 'B', 'T', 'S', 'L', 'U', 'N', 'H'])
def test_recreate_from_data(self, freq):
    org = period_range(start='2001/04/01', freq=freq, periods=1)
    idx = PeriodIndex(org.values, freq=freq)
    tm.assert_index_equal(idx, org)