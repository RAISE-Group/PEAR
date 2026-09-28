def test_string_indexing(self):
    df = pd.DataFrame({'x': range(3)}, index=pd.to_timedelta(range(3), unit='days'))
    expected = df.iloc[0]
    sliced = df.loc['0 days']
    tm.assert_series_equal(sliced, expected)