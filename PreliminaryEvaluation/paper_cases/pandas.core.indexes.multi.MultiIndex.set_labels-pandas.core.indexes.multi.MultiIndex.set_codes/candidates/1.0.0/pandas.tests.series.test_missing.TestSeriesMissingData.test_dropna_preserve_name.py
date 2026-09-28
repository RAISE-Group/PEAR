def test_dropna_preserve_name(self, datetime_series):
    datetime_series[:5] = np.nan
    result = datetime_series.dropna()
    assert result.name == datetime_series.name
    name = datetime_series.name
    ts = datetime_series.copy()
    ts.dropna(inplace=True)
    assert ts.name == name