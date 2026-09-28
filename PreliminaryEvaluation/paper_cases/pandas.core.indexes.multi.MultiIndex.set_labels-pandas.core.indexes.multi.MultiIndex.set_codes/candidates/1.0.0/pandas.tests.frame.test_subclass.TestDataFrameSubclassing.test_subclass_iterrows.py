def test_subclass_iterrows(self):
    df = tm.SubclassedDataFrame({'a': [1]})
    for i, row in df.iterrows():
        assert isinstance(row, tm.SubclassedSeries)
        tm.assert_series_equal(row, df.loc[i])