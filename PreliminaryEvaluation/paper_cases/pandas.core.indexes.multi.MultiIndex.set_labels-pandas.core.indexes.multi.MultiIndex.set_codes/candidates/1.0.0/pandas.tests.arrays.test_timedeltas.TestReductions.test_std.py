def test_std(self):
    tdi = pd.TimedeltaIndex(['0H', '4H', 'NaT', '4H', '0H', '2H'])
    arr = tdi.array
    result = arr.std(skipna=True)
    expected = pd.Timedelta(hours=2)
    assert isinstance(result, pd.Timedelta)
    assert result == expected
    result = tdi.std(skipna=True)
    assert isinstance(result, pd.Timedelta)
    assert result == expected
    result = arr.std(skipna=False)
    assert result is pd.NaT
    result = tdi.std(skipna=False)
    assert result is pd.NaT