@pytest.mark.parametrize('dropna', [True, False])
@pytest.mark.xfail(reason='value_counts not implemented yet.')
def test_value_counts(self, all_data, dropna):
    all_data = all_data[:10]
    if dropna:
        other = np.array(all_data[~all_data.isna()])
    else:
        other = all_data
    result = pd.Series(all_data).value_counts(dropna=dropna).sort_index()
    expected = pd.Series(other).value_counts(dropna=dropna).sort_index()
    tm.assert_series_equal(result, expected)