def test_groupby_extension_no_sort(self, data_for_grouping):
    df = pd.DataFrame({'A': [1, 1, 2, 2, 3, 3, 1, 4], 'B': data_for_grouping})
    result = df.groupby('B', sort=False).A.mean()
    _, index = pd.factorize(data_for_grouping, sort=False)
    index = pd.Index(index, name='B')
    expected = pd.Series([1, 3, 4], index=index, name='A')
    self.assert_series_equal(result, expected)