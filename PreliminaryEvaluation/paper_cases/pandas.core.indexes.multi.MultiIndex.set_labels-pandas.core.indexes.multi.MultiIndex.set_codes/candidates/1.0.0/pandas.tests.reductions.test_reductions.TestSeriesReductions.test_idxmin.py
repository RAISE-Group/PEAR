def test_idxmin(self):
    string_series = tm.makeStringSeries().rename('series')
    string_series[5:15] = np.NaN
    assert string_series[string_series.idxmin()] == string_series.min()
    assert pd.isna(string_series.idxmin(skipna=False))
    nona = string_series.dropna()
    assert nona[nona.idxmin()] == nona.min()
    assert nona.index.values.tolist().index(nona.idxmin()) == nona.values.argmin()
    allna = string_series * np.nan
    assert pd.isna(allna.idxmin())
    s = Series(pd.date_range('20130102', periods=6))
    result = s.idxmin()
    assert result == 0
    s[0] = np.nan
    result = s.idxmin()
    assert result == 1