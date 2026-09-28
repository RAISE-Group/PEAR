def test_npsum(self):
    tdi = pd.TimedeltaIndex(['3H', '3H', '2H', '5H', '4H'])
    arr = tdi.array
    result = np.sum(tdi)
    expected = pd.Timedelta(hours=17)
    assert isinstance(result, pd.Timedelta)
    assert result == expected
    result = np.sum(arr)
    assert isinstance(result, pd.Timedelta)
    assert result == expected