def test_median(self):
    tdi = pd.TimedeltaIndex(['0H', '3H', 'NaT', '5H06m', '0H', '2H'])
    arr = tdi.array
    result = arr.median(skipna=True)
    expected = pd.Timedelta(hours=2)
    assert isinstance(result, pd.Timedelta)
    assert result == expected
    result = tdi.median(skipna=True)
    assert isinstance(result, pd.Timedelta)
    assert result == expected
    result = arr.std(skipna=False)
    assert result is pd.NaT
    result = tdi.std(skipna=False)
    assert result is pd.NaT