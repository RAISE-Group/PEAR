def test_idxmax(self):
    string_series = tm.makeStringSeries().rename('series')
    string_series[5:15] = np.NaN
    assert string_series[string_series.idxmax()] == string_series.max()
    assert pd.isna(string_series.idxmax(skipna=False))
    nona = string_series.dropna()
    assert nona[nona.idxmax()] == nona.max()
    assert nona.index.values.tolist().index(nona.idxmax()) == nona.values.argmax()
    allna = string_series * np.nan
    assert pd.isna(allna.idxmax())
    from pandas import date_range
    s = Series(date_range('20130102', periods=6))
    result = s.idxmax()
    assert result == 5
    s[5] = np.nan
    result = s.idxmax()
    assert result == 4
    s = pd.Series([1, 2, 3], [1.1, 2.1, 3.1])
    result = s.idxmax()
    assert result == 3.1
    result = s.idxmin()
    assert result == 1.1
    s = pd.Series(s.index, s.index)
    result = s.idxmax()
    assert result == 3.1
    result = s.idxmin()
    assert result == 1.1