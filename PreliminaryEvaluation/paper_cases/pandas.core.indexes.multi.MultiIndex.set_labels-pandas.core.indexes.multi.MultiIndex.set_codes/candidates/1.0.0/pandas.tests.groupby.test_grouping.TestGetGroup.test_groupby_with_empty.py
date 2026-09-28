def test_groupby_with_empty(self):
    index = pd.DatetimeIndex(())
    data = ()
    series = pd.Series(data, index, dtype=object)
    grouper = pd.Grouper(freq='D')
    grouped = series.groupby(grouper)
    assert next(iter(grouped), None) is None