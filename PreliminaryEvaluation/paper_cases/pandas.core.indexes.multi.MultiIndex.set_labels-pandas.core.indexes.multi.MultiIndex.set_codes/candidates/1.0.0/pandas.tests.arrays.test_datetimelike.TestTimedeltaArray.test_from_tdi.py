def test_from_tdi(self):
    tdi = pd.TimedeltaIndex(['1 Day', '3 Hours'])
    arr = TimedeltaArray(tdi)
    assert list(arr) == list(tdi)
    tdi2 = pd.Index(arr)
    assert isinstance(tdi2, pd.TimedeltaIndex)
    assert list(tdi2) == list(arr)