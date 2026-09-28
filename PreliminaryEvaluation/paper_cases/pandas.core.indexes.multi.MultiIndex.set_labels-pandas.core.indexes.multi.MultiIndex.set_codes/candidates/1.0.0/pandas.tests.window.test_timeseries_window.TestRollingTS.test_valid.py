def test_valid(self):
    df = self.regular
    with pytest.raises(ValueError):
        df.rolling(window='foobar')
    with pytest.raises(ValueError):
        df.reset_index().rolling(window='foobar')
    for freq in ['2MS', offsets.MonthBegin(2)]:
        with pytest.raises(ValueError):
            df.rolling(window=freq)
    for freq in ['1D', offsets.Day(2), '2ms']:
        df.rolling(window=freq)
    for minp in [1.0, 'foo', np.array([1, 2, 3])]:
        with pytest.raises(ValueError):
            df.rolling(window='1D', min_periods=minp)
    with pytest.raises(NotImplementedError):
        df.rolling(window='1D', center=True)