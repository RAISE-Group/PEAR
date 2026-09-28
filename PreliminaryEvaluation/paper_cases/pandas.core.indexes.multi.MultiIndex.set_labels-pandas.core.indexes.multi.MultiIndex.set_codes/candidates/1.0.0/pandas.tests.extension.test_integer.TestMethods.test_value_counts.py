@pytest.mark.skip(reason='uses nullable integer')
def test_value_counts(self, all_data, dropna):
    all_data = all_data[:10]
    if dropna:
        other = np.array(all_data[~all_data.isna()])
    else:
        other = all_data
    result = pd.Series(all_data).value_counts(dropna=dropna).sort_index()
    expected = pd.Series(other).value_counts(dropna=dropna).sort_index()
    expected.index = expected.index.astype(all_data.dtype)
    self.assert_series_equal(result, expected)