@pytest.mark.parametrize('ascending', [True, False])
def test_sort_values_missing(self, data_missing_for_sorting, ascending):
    ser = pd.Series(data_missing_for_sorting)
    result = ser.sort_values(ascending=ascending)
    if ascending:
        expected = ser.iloc[[2, 0, 1]]
    else:
        expected = ser.iloc[[0, 2, 1]]
    self.assert_series_equal(result, expected)