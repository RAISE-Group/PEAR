def test_from_pi(self, period_index):
    pi = period_index
    arr = PeriodArray(pi)
    assert list(arr) == list(pi)
    pi2 = pd.Index(arr)
    assert isinstance(pi2, pd.PeriodIndex)
    assert list(pi2) == list(arr)