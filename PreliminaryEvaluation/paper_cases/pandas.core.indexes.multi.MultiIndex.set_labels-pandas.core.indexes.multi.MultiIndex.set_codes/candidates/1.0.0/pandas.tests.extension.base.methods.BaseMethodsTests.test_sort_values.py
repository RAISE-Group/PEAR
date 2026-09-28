@pytest.mark.parametrize('ascending', [True, False])
def test_sort_values(self, data_for_sorting, ascending):
    ser = pd.Series(data_for_sorting)
    result = ser.sort_values(ascending=ascending)
    expected = ser.iloc[[2, 0, 1]]
    if not ascending:
        expected = expected[::-1]
    self.assert_series_equal(result, expected)